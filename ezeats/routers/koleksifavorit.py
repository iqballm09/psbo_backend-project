# Import libraries
from requests import Session
from ezeats import models, schemas
from .koleksisaya import KoleksiSaya
from ezeats.database import engine, get_db
from fastapi import Depends, FastAPI, status, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

# Initiate app and router
app = FastAPI()
router = InferringRouter()
models.Base.metadata.create_all(engine)

@cbv(router)
class KoleksiFavorit(KoleksiSaya):
    session: Session = Depends(get_db)

    ## Create
    @router.post("/profile/koleksi-favorit", status_code=status.HTTP_201_CREATED, tags=['koleksi favorit'])
    def create(self, item: schemas.KoleksiFavorit):
        new_item = models.KoleksiFavorit(status=item.status, jam=item.jam, tanggal=item.tanggal)
        self.session.add(new_item)
        self.session.commit()          
        return new_item

    ## Read
    @router.get('/profile/koleksi-favorit', tags=['koleksi favorit'])
    def show_all(self):
        list_koleksi = self.session.query(models.KoleksiFavorit).all()
        return list_koleksi    
    
    @router.get('/profile/koleksi-favorit/{id}', status_code=status.HTTP_200_OK, tags=['koleksi favorit'])
    def show_by_id(self, id):
        koleksi = self.session.query(models.KoleksiFavorit).filter(models.KoleksiFavorit.id == id).first()
        if not koleksi:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Restoran dengan id = {id} tidak ada di Koleksi Favorit")
        return koleksi

    ## Delete
    @router.delete('/profile/koleksi-favorit/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['koleksi favorit'])
    def destroy(self, id):
        koleksi = self.session.query(models.KoleksiFavorit).filter(models.KoleksiFavorit.id == id).delete(synchronize_session=False)
        if not koleksi:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restoran dengan id = {id} sudah tidak ada di Koleksi Favorit")  
        self.session.commit()
        return f"Restoran sudah dihapus dari Koleksi Favorit"

app.include_router(router)