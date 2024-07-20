import time
from typing import Dict

import jwt


def token_response(token: str):
    return {
        "success": True,
        "message": "Access token",
        "data": {
            "access_token": token,
        }
    }


JWT_SECRET = "fwlklkojerj23fj&nalns"


def signJWT(id: str) -> Dict[str, str]:
    # Set the expiry time.
    
    payload = {
        'id': id,
        'expires': time.time() + 2592000
    }
    return token_response(jwt.encode(payload, JWT_SECRET, algorithm="HS256"))


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token, JWT_SECRET, algorithms="HS256")
        return decoded_token if decoded_token['expires'] >= time.time() else None
    except:
        return {}
