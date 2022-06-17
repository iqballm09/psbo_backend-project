# Import libraries
from . import models, database
from fastapi import FastAPI
from .routers import koleksifavorit, daftarhitam, histori, review, resto, user, authentication

app = FastAPI()
models.Base.metadata.create_all(database.engine)

app.include_router(authentication.router)
app.include_router(daftarhitam.router)
app.include_router(koleksifavorit.router)
app.include_router(histori.router)
app.include_router(review.router)
app.include_router(resto.router)
app.include_router(user.router)

