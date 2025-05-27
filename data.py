from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional, List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    region: str
    postal_code: str
    country: str

class Company(BaseModel):
    name: str
    industry: str
    description: str
    website: Optional[HttpUrl] = None

class Profile(BaseModel):
    username: str
    full_name: str
    bio: str
    status_message: str
    job_title: str
    department: str
    interests: List[str]
    skills: List[str]
    favorite_quote: Optional[str] = None
    notes: Optional[str] = None

class UserFull(BaseModel):
    id: int
    email: EmailStr
    phone: str
    registered_at: datetime
    is_active: bool
    address: Address
    company: Company
    profile: Profile

user_full = UserFull(
    id = 111,
    email = "user@example.com",
    phone = "+7 (867)-812-54-87",
    registered_at = datetime.now(),
    is_active = True,
    address = {
        "street": "ул. Ленина, д.10",
        # "city": "Москва", 
        "region": "Московская область",
        "postal_code": "117402",
        "country": "Россия"
    },
    company = {
        "name": "ООО «ТехноСофт»",
        "industry": "Информационные технологии",
        "description": "Разработка программного обеспечения",
        "website": "https://technosoft.ru"
    },
    profile = {
        "username": "userer",
        "fullname": "Пользователь Иванов",
        "bio": "Студент",
        "status_message": "Работаю над новым проектом",
        "job_title": "Junior-разработчик",
        "department": "Отдел разработки",
        "interests": ["Программирование", "Искусственный интеллект", "Брейнрот"],
        "skills": ["Python", "Django", "FastAPI"],
        "favorite_quote": "Тунг Тунг Тунг Сахур",
        "notes": "Участвует в наставничестве новых сотрудников"
    }
)

print(user_full)