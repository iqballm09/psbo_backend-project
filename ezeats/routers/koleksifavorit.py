# Import libraries
from requests import Session
from .. import models, schemas, cbv
from .koleksisaya import KoleksiSaya
from .. database import engine, get_db
from fastapi import Depends, FastAPI, status, HTTPException, APIRouter

# Initiate app and router
app = FastAPI()
router = APIRouter(
    tags=["Koleksi Favorit"],
    prefix="/koleksi-favorit"
)
models.Base.metadata.create_all(engine)

@cbv.cbv(router)
class KoleksiFavorit(KoleksiSaya):
    session: Session = Depends(get_db)

    ## Create
    @router.post("/", status_code=status.HTTP_201_CREATED)
    def create(self, item: schemas.KoleksiFavorit):
        new_item = models.KoleksiFavorit(status=item.status, user_id=1, resto_id=1, jam=item.jam, tanggal=item.tanggal)
        self.session.add(new_item)
        self.session.commit()          
        return new_item

    ## Read
    @router.get('/')
    def show_all(self):
        list_koleksi = self.session.query(models.KoleksiFavorit).all()
        return list_koleksi    
    
    @router.get('/{id}', status_code=status.HTTP_200_OK)
    def show_by_id(self, id):
        koleksi = self.session.query(models.KoleksiFavorit).filter(models.KoleksiFavorit.id == id).first()
        if not koleksi:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Restoran dengan id = {id} tidak ada di Koleksi Favorit")
        return koleksi

    ## Delete
    @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
    def destroy(self, id):
        koleksi = self.session.query(models.KoleksiFavorit).filter(models.KoleksiFavorit.id == id).delete(synchronize_session=False)
        if not koleksi:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restoran dengan id = {id} sudah tidak ada di Koleksi Favorit")  
        self.session.commit()
        return f"Restoran sudah dihapus dari Koleksi Favorit"

app.include_router(router)