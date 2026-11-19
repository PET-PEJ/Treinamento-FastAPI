from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    name: str = Field(..., max_length=100, description="Nome do Petiano")
    email: EmailStr = Field(...,max_length=150, 
                            description="Email do PETiano", 
                            examples=["usuario@exemplo.com"])
    accronym: str = Field(...,min_length=3,max_length=3, 
                          description="Sigla do PETiano")

class UserCreate(UserBase):
    password: str = Field(...,max_length=100,description="Senha do PETiano")

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    accronym: Optional[str] = None

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True