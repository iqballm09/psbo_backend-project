# Import libraries
from . import models, schemas
from database import engine, get_db
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

# Initiate app and router
app = FastAPI()
router = InferringRouter()
models.Base.metadata.create_all(engine)

@cbv(router)
class KoleksiFavorit:
    session: Session = Depends(get_db)

    ## Create
    @router.post("/profile/koleksi-favorit", status_code=status.HTTP_201_CREATED)
    def create(self, item: schemas.KoleksiFavorit):
        new_item = models.KoleksiFavorit(status=item.status, jam=item.jam, tanggal=item.tanggal)
        self.session.add(new_item)
        self.session.commit()
        return new_item

    ## Read
    @router.get('/profile/koleksi-favorit')
    def all(self):
        list_koleksi = self.session.query(models.KoleksiFavorit).all()
        return list_koleksi

    @router.get('/profile/koleksi-favorit/{id}', status_code=status.HTTP_200_OK)
    def show(self, id):
        koleksi = self.session.query(models.KoleksiFavorit).filter(models.KoleksiFavorit.id == id).first()
        if not koleksi:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Restoran dengan id {id} sudah tidak ada di Koleksi Favorit")
        return koleksi

    # ## Update
    # @router.put('/profile/koleksi-favorit/{id}', status_code=status.HTTP_202_ACCEPTED)
    # def update(self, id, request: schemas.KoleksiFavorit):
    #     koleksi = self.session.query(models.KoleksiFavorit).filter(models.KoleksiFavorit.id == id)
    #     if not koleksi.first():
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
    #                             detail=f"Restoran dengan id {id} sudah tidak ada di Koleksi Favorit")
    #     koleksi.update(request)                                                           
    #     self.session.commit()
    #     return 'updated!'     


    ## Delete
    @router.delete('/profile/koleksi-favorit/{id}', status_code=status.HTTP_204_NO_CONTENT)
    def destroy(self, id):
        koleksi = self.session.query(models.KoleksiFavorit).filter(models.KoleksiFavorit.id == 
                                                                   id).delete(synchronize_session=False)
        self.session.commit()
        return 'done!'
app.include_router(router)