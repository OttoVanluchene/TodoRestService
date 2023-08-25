import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv()

# Connection details for the PostgreSQL database
USERNAME = os.getenv('DB_USERNAME')
PASSWORD = os.getenv('DB_PASSWORD')
HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# Create a PostgreSQL engine instance
engine = create_engine(
    f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}")

# Create a DeclarativeMeta instance
Base = declarative_base()

# Create SessionLocal class from sessionmaker factory
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()