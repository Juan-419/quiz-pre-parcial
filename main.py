from fastapi import FastAPI
from db import create_db_and_tables
from bus import router as bus_router
from destino import router as destino_router


app = FastAPI(title="Transportes sigmotoa")

