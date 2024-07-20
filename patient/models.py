from typing import Optional, List
import base64
from pydantic import BaseModel, Field, EmailStr, validator


class CreatePatient(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    age: int = Field(...)
    gender: str = Field(...)
    

class Document(BaseModel):
    @validator('file')
    def is_base64(data: str) -> bool:
        """
        Checks if a given base64 string is valid or not.
        Call this before passing data to s3
        """
        try:
            base64.b64decode(data.split(";base64,")[1], validate=True)
            return data
        except Exception as e:
            raise ValueError('File is not a valid base64 string', str(e))

    file: str = Field(..., description='base64 converted file')
    name: Optional[str] = Field(None)
    type: Optional[str] = Field("medical_records")
    extension: Optional[str] = Field(None)
    

class Documents(BaseModel):
    documents: List[Document]