from fastapi import Depends, FastAPI
from sqlmodel import Session, SQLModel, create_engine
from typing import Annotated
import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager


load_dotenv()  # Cargar variables de entorno desde .env

# Variables desde el entorno
DB_HOST = os.getenv("DB_HOST", "test_database1")
DB_PORT = os.getenv("DB_PORT", "5411")
DB_NAME = os.getenv("DB_NAME", "test1")
DB_USER = os.getenv("DB_USER", "test_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "test_password")

# Crear engine de PostgreSQL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager
async def init_db(app: FastAPI):
    """Initialize the database."""
    SQLModel.metadata.create_all(engine)
    # your initialization code here
    yield
