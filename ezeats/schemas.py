from pydantic import BaseModel
from typing import List

class KoleksiSaya(BaseModel):
    status: str
    jam: str
    tanggal: str

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

class User(BaseModel):
	email: str
	nama: str
	deskripsi_singkat: str 
	password: str
	no_telp: str
	alamat: str
	gambar: str
	cover: str

