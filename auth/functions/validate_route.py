
from auth.schema import Doctor
from utilities.database import SessionLocal
from sqlalchemy import select


def validate_route(payload):
    """validate the route
    Raise error if doctor not found, else returns the doctor
    
    Args:
        payload ([dict]): having id data extracted from jwt-token
    """
    
    with SessionLocal() as session:
        
        s_query = select(Doctor).where(Doctor.id == payload['id'])
        doctor = session.scalars(s_query).one_or_none()
    
        if not doctor:
            raise ValueError("Doctor not found!")
    
        return {
            "id": doctor.id,
            "name": doctor.name,
            "email": doctor.email,
            "password": doctor.password,
            "speciality": doctor.speciality
        }
