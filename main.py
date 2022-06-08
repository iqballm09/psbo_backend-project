# Import libraries
from fastapi import FastAPI
from database import engine
from routers import models, koleksisaya, koleksifavorit, daftarhitam
from routers.histori import Histori

app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(daftarhitam.router)
app.include_router(koleksifavorit.router)
#app.include_router(histori.router)

