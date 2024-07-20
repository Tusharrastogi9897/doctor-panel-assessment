from fastapi import Body, APIRouter, Depends, Path
from starlette.requests import Request
from .models import *
from auth.functions.jwt_bearer import JWTBearer
from .abstract import abstract_func


router = APIRouter()


@router.post("/add", dependencies=[Depends(JWTBearer(auto_error=False))])
def create_patient_route(request: Request, data: CreatePatient = Body(...)):
    return abstract_func('add_patient', data, request)


@router.get("/list", dependencies=[Depends(JWTBearer(auto_error=False))])
def get_patients_route(request: Request):
    return abstract_func('get_patients', request)


@router.get("/fetch-documents/{patient_id}", dependencies=[Depends(JWTBearer(auto_error=False))])
def get_patient_documents_route(request: Request, patient_id: int = Path(...)):
    return abstract_func('fetch_documents', patient_id, request)


@router.post("/upload-documents/{patient_id}", dependencies=[Depends(JWTBearer(auto_error=False))])
def get_patient_documents_route(request: Request, patient_id: int = Path(...), data: Documents = Body(...)):
    return abstract_func('upload_documents', patient_id, data, request)