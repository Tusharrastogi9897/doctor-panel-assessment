from auth.schema import Doctor
from utilities.database import SessionLocal
from sqlalchemy import select
from passlib.context import CryptContext
from auth.functions.jwt_handler import signJWT


hash_helper = CryptContext(schemes=["bcrypt"])

def user_login(credentials):
    
    credentials = credentials.dict()
    
    with SessionLocal() as session:
        s_query = select(Doctor).where(Doctor.email == credentials['username'])
        
        doctor = session.scalars(s_query).one_or_none()
        
        if doctor:
            password = hash_helper.verify(credentials["password"], doctor.password)
            
            if not password:
                raise ValueError("Email or Password is incorrect!")
        
        else:
            raise ValueError("Email or Password is incorrect!")
        
    
        return signJWT(doctor.id)