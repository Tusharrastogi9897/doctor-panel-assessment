from auth.functions.jwt_handler import decodeJWT
from auth.functions.validate_route import validate_route
from utilities.database import SessionLocal
from sqlalchemy import select
from patient.schema import Patient, Document
from utilities.response_helper import response_helper
from utilities.aws import upload_document


def upload_documents(patient_id, data, request):
    
    data = data.dict()
    
    token = request.state.token
    payload = decodeJWT(token)
    
    doctor = validate_route(payload)
    
    with SessionLocal() as session:
        s_query = select(Patient).where(Patient.id == patient_id)
        
        patient = session.scalars(s_query).one_or_none()
        
        if not patient:
            raise ValueError("Patient not Found!")
        
        else:
            for document in data['documents']:
                document_location = upload_document(document['file'])
                
                _document_ = Document(
                    patient_id=patient.id,
                    doctor_id=doctor['id'],
                    location=document_location,
                    document_type=document['type'],
                    extension=document['extension'],
                    file_name=document['name']
                )
            
                session.add(_document_)
        
        session.commit()
    
    return response_helper(success=True, message="Document added successfuly!")