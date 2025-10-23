from fastapi import APIRouter
from sqlmodel import select
from models import conductor
from utils import get_session

router = APIRouter()

@router.post("/")
def crear_conductor(Conductor: conductor):
    with get_session()as session:
        session.add(Conductor)
        session.commit()
        session.refresh(Conductor)
        return Conductor

@router.get("/")
def listar_conductor()
    with get_session() as session:
        conductor = session.exec(select(conductor)).all()
        return conductor