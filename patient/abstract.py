

from fastapi import HTTPException
from auth.schema import Event
from utilities.database import SessionLocal
from patient.functions.add_patient import add_patient
from patient.functions.get_patients import get_patients
from patient.functions.fetch_documents import fetch_documents
from patient.functions.upload_documents import upload_documents


FUNCTION_LIBRARY = {
    "add_patient": add_patient,
    "get_patients": get_patients,
    "fetch_documents": fetch_documents,
    "upload_documents": upload_documents,
}

def abstract_func(func_name, *args):
    try:
        response = FUNCTION_LIBRARY[func_name](*args)
        
        with SessionLocal() as session:
            event = Event(
                data={
                    "type": func_name,
                    "response": response
                }
            )
            
            session.add(event)
            session.commit()
        
        return response
    
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {e}")
        