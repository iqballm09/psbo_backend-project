from pydantic import BaseModel

class KoleksiSaya(BaseModel):
    status: str = "value"
    jam: str = "value"
    tanggal: str = "value"

class KoleksiFavorit(KoleksiSaya, BaseModel):
    pass

class DaftarHitam(KoleksiSaya, BaseModel):
    pass






class Histori(BaseModel):
    jam: str
    tanggal: str

class Review(BaseModel):
    judul: str
    ulasan: str
    gambar: str
    rekomendasi: str
    jam: str
    tanggal: str
    upvotes: int
    downvotes: int  