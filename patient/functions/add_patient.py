from auth.functions.jwt_handler import decodeJWT
from auth.functions.validate_route import validate_route
from utilities.database import SessionLocal
from sqlalchemy import select
from patient.schema import Patient, PatientDoctor
from utilities.response_helper import response_helper

def add_patient(data, request):
    
    data = data.dict()
    
    token = request.state.token
    payload = decodeJWT(token)
    
    doctor = validate_route(payload)
    
    with SessionLocal() as session:
        s_query = select(Patient).where(Patient.email == data['email'])
        
        patient = session.scalars(s_query).one_or_none()
        
        if patient:
            s_query = select(PatientDoctor).where(PatientDoctor.patient_id == patient.id).where(PatientDoctor.doctor_id == doctor['id'])
            
            patient_doctor = session.scalars(s_query).one_or_none()
            
            if not patient_doctor:
                patient_doctor = PatientDoctor(
                    patient_id=patient.id,
                    doctor_id=doctor['id']
                )
                            
            else:
                raise ValueError("Patient already exists!")
        
        else:
            
            patient = Patient(
                email=data["email"],
                name=data["name"],
                gender=data['gender'],
                age=data['age']
            )
                        
            session.add(patient)
            session.commit()
            
            patient_doctor = PatientDoctor(
                patient_id=patient.id,
                doctor_id=doctor['id']
            )
        
        session.add(patient_doctor)
        session.commit()
    
    return response_helper(success=True, message="Patient added successfuly!", payload=data)