from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.users import User, UserRole
from src.utils import hash_password, verify_password
from src.auth import auth, get_current_user
from src.schemas.scheme import LoginRequest, UserCreate, UserResponse

router = APIRouter(prefix="/auth", tags = ["auth"])

@router.post("/register", response_model = UserResponse, status_code = status.HTTP_201_CREATED)
async def register(user: UserCreate, db: Session = Depends(get_db), response: Response = None):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code = 400, detail = "Такой логин уже существует")
    
    try:
        role_str = user.role.lower()
        role = UserRole(role_str)
    except ValueError:
        raise HTTPException(status_code = 400, detail = "Неправильная речь")
    
    hashed_password = hash_password(user.password)

    db_user = User (
        role = role,
        full_name = user.full_name,
        birth_date = user.birth_date,
        driving_experience = user.driving_experience,
        citizenship = user.citizenship,
        inn = user.inn,
        email = user.email,
        password = hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    token = auth.create_access_token(db_user.email)
    response.set_cookie(
        key = "access_token",
        value = token,
        httponly = True,
        samesite = "none",
        secure = True,
        path = '/'
    )
    return db_user

@router.post("/login")
async def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login_data.email).first()
    if not user or not verify_password(login_data.password, user.password_hash):
        raise HTTPException (
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Неправильный логин или пароль"
        )
    token = auth.create_access_token(uid = user.email)

    response = JSONResponse(content={"message": "Login successful"})
    response.set_cookie(
        key = "access_token",
        value = token,
        httponly = True,
        samesite = "none",
        secure = True,
        path = '/'
    )
    return response

@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key = "access_token")
    return {"message": "Выход выполнен"}

@router.get("/me", response_model = UserResponse)
async def read_users_me (current_user: User = Depends(get_current_user)):
    return current_user