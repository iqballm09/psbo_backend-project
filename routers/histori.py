# Import libraries
from requests import Session
from . import models, schemas
from .koleksisaya import KoleksiSaya
from database import engine, get_db
from fastapi import Depends, FastAPI, status, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

# Initiate app and router
app = FastAPI()
router = InferringRouter()
models.Base.metadata.create_all(engine)

@cbv(router)
class Histori:
    session: Session = Depends(get_db)

    ## Create
    @router.post("/profile/histori", status_code=status.HTTP_201_CREATED)
    def create(self, item: schemas.Histori):
        new_histori = models.Histori(jam=item.jam, tanggal=item.tanggal)
        self.session.add(new_histori)
        self.session.commit()
        return f"Restoran sudah ditambahkan ke Histori"

    ## Read
    @router.get('/profile/histori')
    def show_all(self):
        list_histori = self.session.query(models.Histori).all()
        return list_histori    
    
    @router.get('/profile/histori/{id}', status_code=status.HTTP_200_OK)
    def show_by_id(self, id):
        histori = self.session.query(models.Histori).filter(models.Histori.id == id).first()
        if not histori:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Restoran dengan id = {id} tidak ada di Histori")
        return histori

    ## Delete
    @router.delete('/profile/histori/{id}', status_code=status.HTTP_204_NO_CONTENT)
    def destroy(self, id):
        koleksi = self.session.query(models.Histori).filter(models.Histori.id == id).delete(synchronize_session=False)
        if not koleksi:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restoran dengan id = {id} sudah tidak ada di Histori")  
        self.session.commit()
        return f"Restoran sudah dihapus dari Histori"

app.include_router(router)