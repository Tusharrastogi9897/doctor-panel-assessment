from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.routes import router as AuthRouter
from patient.routes import router as PatientRouter
from auth.functions.jwt_bearer import JWTBearer


app = FastAPI(docs_url='/api/v1/docs')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


token_listener = JWTBearer()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Doctor Panel API"}


app.include_router(AuthRouter, tags=["Authentication"], prefix="/api/v1/auth")
app.include_router(PatientRouter, tags=["Patient Router"], prefix="/api/v1/patient")
