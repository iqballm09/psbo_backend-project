# Import libraries
from fastapi import FastAPI
from database import engine
from routers import daftarhitam, koleksifavorit, models

app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(daftarhitam.router)
app.include_router(koleksifavorit.router)

