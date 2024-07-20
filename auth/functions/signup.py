from auth.schema import Doctor
from utilities.database import SessionLocal
from sqlalchemy import select
from passlib.context import CryptContext
from auth.functions.jwt_handler import signJWT
from utilities.response_helper import response_helper


hash_helper = CryptContext(schemes=["bcrypt"])

def user_signup(data):
    
    data = data.dict()
    
    with SessionLocal() as session:
        s_query = select(Doctor).where(Doctor.email == data['email'])
        
        doctor = session.scalars(s_query).one_or_none()
        
        if doctor:
            raise ValueError("Doctor already Exists!")
        
        else:
            
            password = hash_helper.encrypt(data["password"])
            
            doctor = Doctor(
                email=data["email"],
                name=data["name"],
                speciality=data["speciality"],
                password=password
            )
            
            session.add(doctor)
            session.commit()
    
        auth_token = signJWT(doctor.id)
        auth_token = auth_token['data']['access_token']
    
        return_data = {
            "user": {
                **data,
                "password": password,
                "id": doctor.id
            },
            "authToken": auth_token
        }
        
        return response_helper(success=True, message="Doctor added successfuly!", data=return_data)