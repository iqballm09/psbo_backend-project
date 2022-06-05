# Import libraries
from . import schemas, models
from database import engine, get_db
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, status, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

# Initiate app and router
app = FastAPI()
router = InferringRouter()
models.Base.metadata.create_all(engine)

@cbv(router)
class DaftarHitam:
    session: Session = Depends(get_db)

    ## Create
    @router.post("/profile/daftar-hitam", status_code=status.HTTP_201_CREATED)
    def create(self, item: schemas.DaftarHitam):
        new_item = models.DaftarHitam(status=item.status, jam=item.jam, tanggal=item.tanggal)
        self.session.add(new_item)
        self.session.commit()
        return new_item

    ## Read
    @router.get('/profile/daftar-hitam')
    def all(self):
        list_koleksi = self.session.query(models.DaftarHitam).all()
        return list_koleksi

    @router.get('/profile/daftar-hitam/{id}', status_code=status.HTTP_200_OK)
    def show(self, id):
        koleksi = self.session.query(models.DaftarHitam).filter(models.DaftarHitam.id == id).first()
        if not koleksi:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Restoran dengan id {id} sudah tidak ada di Daftar Hitam")
        return koleksi

    ## Delete
    @router.delete('/profile/daftar-hitam/{id}', status_code=status.HTTP_204_NO_CONTENT)
    def destroy(self, id):
        koleksi = self.session.query(models.DaftarHitam).filter(models.DaftarHitam.id == 
                                                                   id).delete(synchronize_session=False)
        self.session.commit()
        return 'done!'
app.include_router(router)