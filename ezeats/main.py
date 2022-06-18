# Import libraries
from ezeats import models
from ezeats import database
from fastapi import FastAPI
from ezeats.routers import koleksifavorit, daftarhitam, histori, review, resto, user, authentication

app = FastAPI()
models.Base.metadata.create_all(database.engine)

app.include_router(authentication.router)
app.include_router(daftarhitam.router)
app.include_router(koleksifavorit.router)
app.include_router(histori.router)
app.include_router(review.router)
app.include_router(resto.router)
app.include_router(user.router)