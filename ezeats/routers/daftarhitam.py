# Import libraries
from requests import Session
from .. import models, schemas, cbv
from .koleksisaya import KoleksiSaya
from .. database import engine, get_db
from fastapi import Depends, FastAPI, status, HTTPException, APIRouter

# Initiate app and router
app = FastAPI()
router = APIRouter(
    prefix="/daftar-hitam",
    tags=["Daftar Hitam"]
)
models.Base.metadata.create_all(engine)

@cbv.cbv(router)
class DaftarHitam(KoleksiSaya):
    session: Session = Depends(get_db)

    ## Create
    @router.post("/", status_code=status.HTTP_201_CREATED)
    def create(self, item: schemas.DaftarHitam):
        new_item = models.DaftarHitam(user_id=1, resto_id=1, status=item.status, jam=item.jam, tanggal=item.tanggal)
        self.session.add(new_item)
        self.session.commit()          
        return f"Restoran sudah ditambahkan ke Daftar Hitam"

    ## Read
    @router.get("/")
    def show_all(self):
        list_koleksi = self.session.query(models.DaftarHitam).all()
        return list_koleksi    
    
    @router.get('/{id}', status_code=status.HTTP_200_OK)
    def show_by_id(self, id):
        koleksi = self.session.query(models.DaftarHitam).filter(models.DaftarHitam.id == id).first()
        if not koleksi:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Restoran dengan id = {id} tidak ada di Daftar Hitam")
        return koleksi

    ## Delete
    @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
    def destroy(self, id):
        koleksi = self.session.query(models.DaftarHitam).filter(models.DaftarHitam.id == id).delete(synchronize_session=False)
        self.session.commit()
        if not koleksi:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restoran dengan id = {id} sudah tidak ada di Daftar Hitam")           
        return "Restoran sudah dihapus dari Daftar Hitam"

app.include_router(router)