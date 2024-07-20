

from fastapi import HTTPException
from auth.functions.login import user_login
from auth.functions.signup import user_signup
from auth.functions.get_profile import get_profile
from auth.schema import Event
from utilities.database import SessionLocal


FUNCTION_LIBRARY = {
    'user_login': user_login,
    'user_signup': user_signup,
    'get_profile': get_profile
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
        