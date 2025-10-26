from fastapi import FastAPI
from routes import test, calificaciones

app = FastAPI(
    title="API de calificaciones",
    description="API para gestionar calificaciones utilizando FastAPI",
    version="1.0.0"
)

app.include_router(test.router, prefix="/test", tags=["test"])
app.include_router(calificaciones.router, prefix="/calificaciones", tags=["calificaciones"])