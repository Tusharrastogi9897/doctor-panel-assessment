from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv()

# Get the database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Ensure DATABASE_URL is set
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set")

# Create an engine
engine = create_engine(DATABASE_URL)  # Set echo=True for SQL logs

# Define the Base
Base = declarative_base()

# Create tables
Base.metadata.create_all(bind=engine)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def get_all_doctors():
#     with SessionLocal() as session:
#         # test_doc = Doctor(
#         #     name="Test"
#         # )
#         # session.add(test_doc)
#         # session.commit()
        
#         doctors = session.query(Doctor).all()
#         return doctors

# if __name__ == "__main__":
#     doctors = get_all_doctors()
#     print(doctors)
#     for doctor in doctors:
#         print(f"ID: {doctor.id}, Name: {doctor.name}, Email: {doctor.email}, Speciality: {doctor.speciality}")
