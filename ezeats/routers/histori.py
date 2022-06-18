# Import libraries
from requests import Session
from ezeats import models, schemas, cbv
from ezeats.database import engine, get_db
from fastapi import Depends, FastAPI, status, HTTPException, APIRouter

# Initiate app and router
app = FastAPI()
router = APIRouter(
    prefix="/histori",
    tags=["Histori"]
)
models.Base.metadata.create_all(engine)

@cbv.cbv(router)
class Histori:
    session: Session = Depends(get_db)

    ## Create
    @router.post("/", status_code=status.HTTP_201_CREATED)
    def create(self, item: schemas.Histori):
        new_histori = models.Histori(jam=item.jam, user_id=1, resto_id=1, tanggal=item.tanggal)
        self.session.add(new_histori)
        self.session.commit()
        return f"Restoran sudah ditambahkan ke Histori"

    ## Read
    @router.get('/')
    def show_all(self):
        list_histori = self.session.query(models.Histori).all()
        return list_histori    
    
    @router.get('/{id}', status_code=status.HTTP_200_OK)
    def show_by_id(self, id):
        histori = self.session.query(models.Histori).filter(models.Histori.id == id).first()
        if not histori:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Restoran dengan id = {id} tidak ada di Histori")
        return histori

    ## Delete
    @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
    def destroy(self, id):
        koleksi = self.session.query(models.Histori).filter(models.Histori.id == id).delete(synchronize_session=False)
        if not koleksi:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restoran dengan id = {id} sudah tidak ada di Histori")  
        self.session.commit()
        return f"Restoran sudah dihapus dari Histori"

app.include_router(router)