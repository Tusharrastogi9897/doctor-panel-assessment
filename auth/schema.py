from utilities.database import Base
from sqlalchemy import Integer, String, Column, JSON, DateTime
import datetime
from sqlalchemy.orm import relationship


class Doctor(Base):
    __tablename__ = 'doctors'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    speciality = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now)

    patient_doctor = relationship("PatientDoctor", back_populates="doctor")
    documents = relationship("Document", back_populates="doctor")


class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON)  # Column to store a dynamic dictionary
    created_at = Column(DateTime, default=datetime.datetime.now)
    
    

from utilities.database import engine
Base.metadata.create_all(bind=engine)