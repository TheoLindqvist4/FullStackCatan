from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from app.models.database import BaseSQL, engine, User, SessionLocal, get_user_by_id
from app import routers
from starlette.middleware.cors import CORSMiddleware
from starlette_exporter import PrometheusMiddleware, handle_metrics
from jose import JWTError, jwt
from app.models import database, db
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
import secrets


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# JWT Secret and Algorithm
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"

# OAuth2PasswordBearer for token extraction
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=1)  # Set token expiry time (e.g., 1 hour)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
    request: Request = None
):
    if not token and request:
        token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    try:
        payload = jwt.decode(token.replace("Bearer ", ""), SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        user = get_user_by_id(db, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

# FastAPI app instance
app = FastAPI(
    title="My title",
    description="My description",
    version="0.0.1",
)

# Set up templates and static directories
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# CORS settings
origins = [
    "http://localhost:4200",
    "http://localhost:3000",
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(routers.PostRouter)
app.include_router(routers.HealthRouter)

# Prometheus Monitoring
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

# Database initialization on startup
@app.on_event("startup")
async def startup_event():
    BaseSQL.metadata.create_all(bind=engine)

# Route for the root page
@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Route for the play page
@app.get("/play", response_class=HTMLResponse)
async def read_play(request: Request):
    return templates.TemplateResponse("play.html", {"request": request})

@app.get("/profile")
async def profile(request: Request, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    if not current_user:
        return RedirectResponse("/login", status_code=303)
    return templates.TemplateResponse("profile.html", {"request": request, "user": current_user})

# Route for the login page
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(
    request: Request, 
    email: str = Form(...), 
    password: str = Form(...), 
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.email == email).first()
    if not user or user.password != password:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # Create a token
    access_token = create_access_token(data={"sub": str(user.id)})
    
    # Store token in cookies (optional) and redirect to profile
    response = RedirectResponse(url="/profile", status_code=303)
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return response

# Route for the signup page
@app.get("/signup", response_class=HTMLResponse)
async def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

# Route to handle signup submissions
@app.post("/signup")
async def signup(
    request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
    db: Session = Depends(get_db),
):
    if password != confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create a new user
    new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Redirect to login page after successful registration
    return templates.TemplateResponse("login.html", {"request": request, "message": "Account created successfully!"})