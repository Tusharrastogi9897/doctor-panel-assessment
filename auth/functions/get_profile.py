from auth.functions.jwt_handler import decodeJWT
from auth.functions.validate_route import validate_route
from utilities.response_helper import response_helper

def get_profile(request):
    
    token = request.state.token
    payload = decodeJWT(token)
    
    doctor = validate_route(payload)
    
    return response_helper(success=True, data=doctor, message="Doctor profile found!")