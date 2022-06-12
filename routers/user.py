# Import libraries
from requests import Session
from . import models, schemas
from database import engine, get_db
from fastapi import Depends, FastAPI, status, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

# Initiate app and router
app = FastAPI()
router = InferringRouter()
models.Base.metadata.create_all(engine)

@cbv(router)
class User:
    session: Session = Depends(get_db)

    ## Create
    @router.post("/profile/user", status_code=status.HTTP_201_CREATED)
    def create(self, item: schemas.User):
        new_user = models.User(email = item.email, nama = item.nama, deskripsi_singkat = item.deskripsi_singkat, 
                                    password = item.password, no_telp = item.no_telp, alamat = item.alamat, 
                                    gambar = item.gambar, cover = item.cover)
        self.session.add(new_user)
        self.session.commit()
        return f"User sudah ditambahkan"

    ## Read
    @router.get('/profile/user')
    def show_all(self):
        list_user = self.session.query(models.User).all()
        return list_user    
    
    @router.get('/profile/user/{id}', status_code=status.HTTP_200_OK)
    def show_by_id(self, id):
        user = self.session.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Tidak ditemukan User dengan id = {id}")
        return user

    ## Update
    @router.put('/profile/user/{id}', status_code=status.HTTP_202_ACCEPTED)
    def update(self, id, request: schemas.User):
        user = self.session.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f"User dengan id = {id} sudah diupdate")
        else:
            user.email = request.email
            user.nama = request.nama
            user.deskripsi_singkat = request.deskripsi_singkat
            user.password = request.password
            user.no_telp = request.no_telp
            user.alamat = request.alamat
            user.gambar = request.gambar
            user.cover = request.cover
            # user.update(request.dict())                                                           
            self.session.commit()
            self.session.refresh(user)
            return 'updated!'        

    ## Delete
    @router.delete('/profile/user/{id}', status_code=status.HTTP_204_NO_CONTENT)
    def destroy(self, id):
        koleksi = self.session.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
        if not koleksi:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Tidak ada User dengan id = {id}")
        self.session.commit(synchronize_session=False)
        return f"User sudah dihapus dari List User"

app.include_router(router)
