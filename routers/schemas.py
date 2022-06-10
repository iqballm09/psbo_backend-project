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

class Resto(BaseModel):
    nama: str
    kategori: str
    harga: int
    jam_buka: str
    jam_tutup: str
    fasilitas: str
    deskripsi: str
    jalan: str
    kecamatan: str
    kotakab: str
    nama_kabkota: str
    provinsi: str
    web: str
    foto_menu: str
    foto_cover: str
    foto_resto: str
    no_telp: str
    upvotes: int
    downvotes: int