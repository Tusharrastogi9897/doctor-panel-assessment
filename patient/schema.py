from utilities.database import Base
from sqlalchemy import Integer, String, Column, ForeignKey, DateTime
import datetime
from sqlalchemy.orm import relationship


class Patient(Base):
    __tablename__ = 'patients'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)
    gender = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now)

    patient_doctor = relationship("PatientDoctor", back_populates="patient")
    documents = relationship("Document", back_populates="patient")


class PatientDoctor(Base):
    __tablename__ = 'patient_doctor'
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    
    patient = relationship("Patient", back_populates="patient_doctor")
    doctor = relationship("Doctor", back_populates="patient_doctor")


class Document(Base):
    __tablename__ = 'documents'
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    location = Column(String, nullable=False)
    document_type = Column(String)
    extension = Column(String)
    file_name = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now)
    
    patient = relationship("Patient", back_populates="documents")
    doctor = relationship("Doctor", back_populates="documents")
    

from utilities.database import engine
Base.metadata.create_all(bind=engine)
