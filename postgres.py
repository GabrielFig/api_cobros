from fastapi import Depends, FastAPI
from sqlmodel import Session, SQLModel, create_engine
from typing import Annotated
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde .env

# Variables desde el entorno
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "mydatabase")
DB_USER = os.getenv("DB_USER", "myuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "mypassword")

# Crear engine de PostgreSQL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

def init_db(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
