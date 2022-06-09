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
class Review:
    session: Session = Depends(get_db)

    ## Create
    @router.post("/profile/review", status_code=status.HTTP_201_CREATED)
    def create(self, item: schemas.Review):
        new_review = models.Review(judul = item.judul, ulasan = item.ulasan, gambar = item.gambar, 
                                    rekomendasi = item.rekomendasi, jam = item.jam, tanggal = item.tanggal, 
                                    upvotes = item.upvotes, downvotes = item.downvotes)
        self.session.add(new_review)
        self.session.commit()
        return f"Review sudah ditambahkan"

    ## Read
    @router.get('/profile/review')
    def show_all(self):
        list_review = self.session.query(models.Review).all()
        return list_review    
    
    @router.get('/profile/review/{id}', status_code=status.HTTP_200_OK)
    def show_by_id(self, id):
        review = self.session.query(models.Review).filter(models.Review.id == id).first()
        if not review:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Tidak ditemukan Review dengan id = {id}")
        return review

    ## Update
    @router.put('/profile/review/{id}', status_code=status.HTTP_202_ACCEPTED)
    def update(self, id, request: schemas.Review):
        review = self.session.query(models.Review).filter(models.Review.id == id).first()
        if not review:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f"Restoran dengan id = {id} sudah tidak ada di Koleksi Favorit")
        else:
            review.judul = request.judul
            review.ulasan = request.ulasan
            review.gambar = request.gambar
            review.rekomendasi = request.rekomendasi
            review.jam = request.jam
            review.tanggal = request.tanggal
            review.upvotes = request.upvotes
            review.downvotes = request.downvotes
            # review.update(request.dict())                                                           
            self.session.commit()
            self.session.refresh(review)
            return 'updated!'        

    ## Delete
    @router.delete('/profile/review/{id}', status_code=status.HTTP_204_NO_CONTENT)
    def destroy(self, id):
        koleksi = self.session.query(models.Review).filter(models.Review.id == id).delete(synchronize_session=False)
        if not koleksi:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Tidak ada Review dengan id = {id}")
        self.session.commit(synchronize_session=False)
        return f"Review sudah dihapus dari List Review"

app.include_router(router)