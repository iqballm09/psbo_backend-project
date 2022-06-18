from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ezeats import database

Base = database.Base

class KoleksiSaya(Base):
    __tablename__ = "KoleksiSaya"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    jam = Column(String)
    tanggal = Column(String)

class KoleksiFavorit(KoleksiSaya):
    __tablename__ = "KoleksiFavorit"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    resto_id = Column(Integer, ForeignKey('Resto.id'))
    status = Column(String)
    jam = Column(String)
    tanggal = Column(String)

    users = relationship("User", back_populates="koleksi_favorit")
    resto = relationship("Resto", back_populates="koleksi_favorit")

    __mapper_args__ = {
        "concrete": True,
    }

class DaftarHitam(KoleksiSaya):
    __tablename__ = "DaftarHitam"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    resto_id = Column(Integer, ForeignKey('Resto.id'))
    status = Column(String)
    jam = Column(String)
    tanggal = Column(String)

    users = relationship("User", back_populates="daftar_hitam")
    resto = relationship("Resto", back_populates="daftar_hitam")

    __mapper_args__ = {
        "concrete": True,
    }

class Histori(Base):
    __tablename__ = 'Histori'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    resto_id = Column(Integer, ForeignKey('Resto.id'))
    jam = Column(String)
    tanggal = Column(String)

    users = relationship("User", back_populates="histori")
    resto = relationship("Resto", back_populates="histori")

class Review(Base):
    __tablename__ = 'Review'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    resto_id = Column(Integer, ForeignKey('Resto.id'))
    judul = Column(String)
    ulasan = Column(String)
    gambar = Column(String)
    rekomendasi = Column(String)
    jam = Column(String)
    tanggal = Column(String)
    upvotes = Column(Integer)
    downvotes = Column(Integer)

    users = relationship("User", back_populates="review")
    resto = relationship("Resto", back_populates="review")

class Resto(Base):
    __tablename__ = 'Resto' 
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('User.id'))
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

    users = relationship("User", back_populates="resto")
    histori = relationship("Histori", back_populates="resto")
    review = relationship("Review", back_populates="resto")
    daftar_hitam = relationship("DaftarHitam", back_populates="resto")
    koleksi_favorit = relationship("KoleksiFavorit", back_populates="resto")

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

    resto = relationship("Resto", back_populates="users")
    histori = relationship("Histori", back_populates="users")
    review = relationship("Review", back_populates="users")
    daftar_hitam = relationship("DaftarHitam", back_populates="users")
    koleksi_favorit = relationship("KoleksiFavorit", back_populates="users")