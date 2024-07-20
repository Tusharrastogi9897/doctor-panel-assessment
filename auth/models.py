from typing import Optional, List

from pydantic import BaseModel, Field, EmailStr, validator

class SignUpModel(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    speciality: str = Field(...)
