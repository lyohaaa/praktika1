import traceback
from authx import AuthX, AuthXConfig, TokenPayload
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.users import User, UserRole

authx_config = AuthXConfig(
    JWT_ALGORITHM = "HS256",
    JWT_SECRET_KEY = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
    JWT_TOKEN_LOCATION = ["cookies"],
    JWT_ACCESS_COOKIE_NAME = "access_token",
    JWT_COOKIE_CSRF_PROTECT = False
)

auth = AuthX(config = authx_config)

async def get_current_user(payload: TokenPayload = Depends(auth.access_token_required), db: Session = Depends(get_db)):
    try:
        email = payload.sub
        if not email:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Недействительный токен")
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь не найден")
        return user
    except Exception as e:
        print(f"Ошибка: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Не удалось проверить учётные данные")
    
def require_role(required_role: UserRole):
    async def check_role(current_user: User = Depends(get_current_user)):
        if not current_user:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Недействительный токен или пользователь не найден"
            )
        if current_user.role != required_role:
            raise HTTPException(
                status_code = status.HTTP_403_FORBIDDEN,
                detail = f"Требуется роль {required_role.value}"
            )
        return current_user
    return check_role