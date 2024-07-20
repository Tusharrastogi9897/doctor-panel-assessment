from auth.functions.jwt_handler import decodeJWT
from auth.functions.validate_route import validate_route
from utilities.database import SessionLocal
from sqlalchemy import select
from patient.schema import PatientDoctor
from utilities.response_helper import response_helper

def get_patients(request):
        
    token = request.state.token
    payload = decodeJWT(token)
    
    doctor = validate_route(payload)
    
    patient_list = []
    
    with SessionLocal() as session:
        s_query = select(PatientDoctor)\
            .join(PatientDoctor.patient)\
            .where(PatientDoctor.doctor_id == doctor['id'])
        
        patients = session.scalars(s_query).all()
        
        for patient in patients:
            patient_list.append({
                "id": patient.id,
                "name": patient.patient.name,
                "email": patient.patient.email,
                "gender": patient.patient.gender,
                'age': patient.patient.age
            })
    
    return response_helper(success=True, data=patient_list)