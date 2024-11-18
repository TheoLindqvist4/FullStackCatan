from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from app.models.database import BaseSQL, engine, User, SessionLocal
from app import routers
from starlette.middleware.cors import CORSMiddleware
from starlette_exporter import PrometheusMiddleware, handle_metrics

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

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route for the root page
@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Additional template routes
@app.get("/play", response_class=HTMLResponse)
async def read_play(request: Request):
    return templates.TemplateResponse("play.html", {"request": request})

@app.get("/profile", response_class=HTMLResponse)
async def read_profile(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})

# Route for the login page
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Route to handle login submissions
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
    return templates.TemplateResponse("home.html", {"request": request, "user": user})

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
