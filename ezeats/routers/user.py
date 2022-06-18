# Import libraries
from requests import Session
from ezeats import models, schemas, hashing, cbv
from ezeats.database import engine, get_db
from fastapi import Depends, FastAPI, status, HTTPException, APIRouter
from typing import List

# Initiate app and router
app = FastAPI()
router = APIRouter(
    tags=["Users"],
    prefix="/user"
)
models.Base.metadata.create_all(engine)

@cbv.cbv(router)
class User:
    session: Session = Depends(get_db)
    
    ## Create
    @router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
    def create(self,item: schemas.User):
        new_user = models.User(email = item.email, nama = item.nama, deskripsi_singkat = item.deskripsi_singkat, 
                                password = hashing.Hash.bcrypt(item.password), no_telp = item.no_telp, alamat = item.alamat, 
                                gambar = item.gambar, cover = item.cover)
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user

    ## Read
    @router.get('/', response_model=List[schemas.UserOut])
    def show_all(self):
        list_user = self.session.query(models.User).all()
        return list_user    
    
    @router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.UserOut)
    def show_by_id(self, id):
        user = self.session.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Tidak ditemukan User dengan id = {id}")
        return user

    ## Update
    @router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
    def update(self, id, request: schemas.User):
        user = self.session.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f"User dengan id = {id} tidak ditemukan")
        user.update(request.dict())                                                           
        self.session.commit()
        self.session.refresh(user)
        return user

    ## Delete
    @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
    def destroy(self, id):
        koleksi = self.session.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
        if not koleksi:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Tidak ada User dengan id = {id}")
        self.session.commit()
        return f"User sudah dihapus dari List User"

app.include_router(router)
