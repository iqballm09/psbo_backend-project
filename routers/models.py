from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class KoleksiSaya(Base):
    __tablename__ = "KoleksiSaya"
    id = Column(Integer, primary_key=True)
    status = Column(String)
    jam = Column(String)
    tanggal = Column(String)

class KoleksiFavorit(KoleksiSaya):
    __tablename__ = "KoleksiFavorit"
    id = Column(Integer, primary_key=True)
    status = Column(String)
    jam = Column(String)
    tanggal = Column(String)

    __mapper_args__ = {
        "concrete": True,
    }

class DaftarHitam(KoleksiSaya):
    __tablename__ = "DaftarHitam"
    id = Column(Integer, primary_key=True)
    status = Column(String)
    jam = Column(String)
    tanggal = Column(String)

    __mapper_args__ = {
        "concrete": True,
    }

class Histori(Base):
    __tablename__ = 'Histori'
    id = Column(Integer, primary_key=True, index=True)
    jam = Column(String)
    tanggal = Column(String)

class Review(Base):
    __tablename__ = 'Review'
    id = Column(Integer, primary_key=True, index=True)
    judul = Column(String)
    ulasan = Column(String)
    gambar = Column(String)
    rekomendasi = Column(String)
    jam = Column(String)
    tanggal = Column(String)
    upvotes = Column(Integer)
    downvotes = Column(Integer)

class Resto(Base):
    __tablename__ = 'Resto' 
    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String)
    kategori = Column(String)
    harga = Column(Integer)
    jam_buka = Column(String)
    jam_tutup = Column(String)
    fasilitas = Column(String)
    deskripsi = Column(String)
    jalan = Column(String)
    kecamatan = Column(String)
    kotakab = Column(String)
    nama_kabkota = Column(String)
    provinsi = Column(String)
    web = Column(String)
    foto_menu = Column(String)
    foto_cover = Column(String)
    foto_resto = Column(String)
    no_telp = Column(String)
    upvotes = Column(Integer)
    downvotes = Column(Integer)
    
class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    nama = Column(String)
    deskripsi_singkat = Column(String)
    password = Column(String)
    no_telp = Column(String)
    alamat = Column(String)
    gambar = Column(String)
    cover = Column(String)
