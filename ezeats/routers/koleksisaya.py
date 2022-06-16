# Import libraries
from ezeats import schemas, models
from ezeats.database import get_db, engine
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException, FastAPI
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

# Initiate app and router
app = FastAPI()
router = InferringRouter()
models.Base.metadata.create_all(engine)


@cbv(router)
class KoleksiSaya:
    session: Session = Depends(get_db)
    pass

app.include_router(router)