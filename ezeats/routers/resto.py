# Import libraries
from typing import List
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
class Resto:
    session: Session = Depends(get_db)
    
    ## Create
    @router.post("/resto", status_code=status.HTTP_201_CREATED, tags=['resto'])
    def create(self, item: schemas.Resto):
        new_item = models.Resto(nama = item.nama ,
                                kategori = item.kategori ,
                                harga = item.harga ,
                                user_id = 1,
                                jam_buka = item.jam_buka ,
                                jam_tutup = item.jam_tutup ,
                                fasilitas = item.fasilitas ,
                                deskripsi = item.deskripsi ,
                                jalan = item.jalan ,
                                kecamatan = item.kecamatan ,
                                kotakab = item.kotakab ,
                                nama_kabkota = item.nama_kabkota ,
                                provinsi = item.provinsi ,
                                web = item.web ,
                                foto_menu = item.foto_menu ,
                                foto_cover = item.foto_cover ,
                                foto_resto = item.foto_resto ,
                                no_telp = item.no_telp )
        self.session.add(new_item)
        self.session.commit()          
        return new_item

    ## Read
    @router.get('/resto',tags=['resto'])
    def show_all(self):
        list_resto = self.session.query(models.Resto).all()
        return list_resto    
    
    @router.get('/resto/{id}', status_code=status.HTTP_200_OK, tags=['resto'])
    def show_by_id(self, id):
        resto = self.session.query(models.Resto).filter(models.Resto.id == id).first()
        if not resto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Restoran dengan id = {id} tidak ada")
        return resto

    ## Update
    @router.put('/resto/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['resto'])
    def update(self, id, request: schemas.Resto):
        resto = self.session.query(models.Resto).filter(models.Resto.id == id).first()
        if not resto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f"Resto dengan id = {id} tidak ditemukan")
        resto.update(request.dict())                                                           
        self.session.commit()
        self.session.refresh(resto)
        return resto   

    ## Delete
    @router.delete('/resto/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['resto'])
    def destroy(self, id):
        resto = self.session.query(models.Resto).filter(models.Resto.id == id).delete(synchronize_session=False)
        self.session.commit()
        if not resto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restoran dengan id = {id} tidak ada")           
        return f"Restoran berhasil dihapus"


app.include_router(router)