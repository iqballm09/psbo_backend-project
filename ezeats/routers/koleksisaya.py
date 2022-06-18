# Import libraries
from ezeats import models, cbv
from ezeats.database import get_db, engine
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, APIRouter

# Initiate app and router
app = FastAPI()
router = APIRouter()
models.Base.metadata.create_all(engine)


@cbv.cbv(router)
class KoleksiSaya:
    session: Session = Depends(get_db)
    pass

app.include_router(router)