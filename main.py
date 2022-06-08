# Import libraries
from fastapi import FastAPI
from database import engine
from routers import models, koleksifavorit, daftarhitam, histori

app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(daftarhitam.router)
app.include_router(koleksifavorit.router)
app.include_router(histori.router)

