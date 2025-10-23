from fastapi import FastAPI
from db import create_db_and_tables
from bus import router as bus_router
from destino import router as destino_router
from conductor import router as conductor_router

app = FastAPI(title="Transportes sigmotoa")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(bus_router, prefix="/Bus", tags=["Buses"])
app.include_router(destino_router, prefix="/Destino", tags=["Destino"])
app.include_router(conductor_router, prefix="/Conductor", tags=["Conductor"])
