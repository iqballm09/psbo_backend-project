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