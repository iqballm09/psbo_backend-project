# Import libraries
from ezeats import models, schemas
from fastapi import status, HTTPException

class KoleksiSaya:

    ## Create
    def create(self, item: schemas.KoleksiSaya):
        new_item = models.KoleksiSaya(status=item.status, user_id=1, resto_id=1, jam=item.jam, tanggal=item.tanggal)
        self.session.add(new_item)
        self.session.commit()          
        return new_item

    ## Read
    def show_all(self):
        list_koleksi = self.session.query(models.KoleksiSaya).all()
        return list_koleksi    
    
    def show_by_id(self, id):
        koleksi = self.session.query(models.KoleksiSaya).filter(models.KoleksiSaya.id == id).first()
        if not koleksi:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Restoran dengan id = {id} tidak ada di Koleksi Favorit")
        return koleksi

    ## Delete
    def destroy(self, id):
        koleksi = self.session.query(models.KoleksiSaya).filter(models.KoleksiSaya.id == id).delete(synchronize_session=False)
        if not koleksi:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restoran dengan id = {id} sudah tidak ada di Koleksi Favorit")  
        self.session.commit()
        return f"Restoran sudah dihapus dari Koleksi Favorit"
