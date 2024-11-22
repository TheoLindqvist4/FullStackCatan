from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from starlette.middleware.sessions import SessionMiddleware
from app.models.database import BaseSQL
import random
from app.models.database import engine, SessionLocal
from app.models.db import User, get_db
from pydantic import BaseModel
from typing import List


# FastAPI app instance
app = FastAPI(
    title="My title",
    description="My description",
    version="0.0.1",
)

BaseSQL.metadata.create_all(bind = engine)


# Set up templates and static directories
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# CORS settings
origins = [
    "http://localhost:4200",
    "http://localhost:3000",
    "http://localhost:3001",
]

app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

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

# Route for the login page
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

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
    
    # Randomly assign a profile picture
    profile_pictures = ["image1.png", "image2.png", "image3.png", "image4.png"]
    selected_picture = random.choice(profile_pictures)

    # Create a new user with boards_generated initialized to NULL
    new_user = User(
        first_name = first_name, 
        last_name = last_name, 
        email = email, 
        password=password,
        boards_generated = None,  # Explicitly set to None (optional, default is None)
        profile_picture = selected_picture
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Redirect to login page after successful registration
    return templates.TemplateResponse("login.html", {"request": request, "message": "Account created successfully!"})


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
    # Store user ID in session
    request.session["user_id"] = user.id
    return RedirectResponse("/profile", status_code=303)

@app.get("/profile")
async def profile(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    if not user_id:
        return RedirectResponse("/login", status_code=303)

    # Fetch user information from the database
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return RedirectResponse("/login", status_code=303)

    # Build the full path to the user's profile picture
    profile_picture_path = f"/static/images/profile_pictures/{user.profile_picture}"

    # Render the profile template
    return templates.TemplateResponse("profile.html", {
        "request": request,
        "user": user,
        "profile_picture": profile_picture_path
    })


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    profile_picture: str

    class Config:
        orm_mode = True  # Enables Pydantic to work with ORM objects


@app.get("/users", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    """
    Fetch all users from the database.
    """
    users = db.query(User).all()
    return users
