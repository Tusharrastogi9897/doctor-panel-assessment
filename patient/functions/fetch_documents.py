from auth.functions.jwt_handler import decodeJWT
from auth.functions.validate_route import validate_route
from utilities.database import SessionLocal
from sqlalchemy import select
from patient.schema import Patient, Document
from utilities.response_helper import response_helper
from utilities.aws import get_url


def fetch_documents(patient_id, request):
    
    token = request.state.token
    payload = decodeJWT(token)
    
    doctor = validate_route(payload)
    
    document_list = []
    
    with SessionLocal() as session:
        s_query = select(Patient).where(Patient.id == patient_id)
        
        patient = session.scalars(s_query).one_or_none()
        
        if not patient:
            raise ValueError("Patient not Found!")
        
        else:
            s_query = select(Document)\
            .where(Document.doctor_id == doctor['id'])\
            .where(Document.patient_id == patient.id)
        
            documents = session.scalars(s_query).all()
            
            for document in documents:
                document_url = get_url(document.location)
                
                document_list.append({
                    'url': document_url,
                    'name': document.file_name,
                    'type': document.document_type,
                    'extension': document.extension
                })
    
    return response_helper(success=True, data=document_list)