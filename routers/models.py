from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class KoleksiFavorit(Base):
    __tablename__ = 'KoleksiFavorit'
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    jam = Column(String)
    tanggal = Column(String)

class DaftarHitam(Base):
    __tablename__ = 'DaftarHitam'
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    jam = Column(String)
    tanggal = Column(String)

class Histori(Base):
    __tablename__ = 'Histori'
    id = Column(Integer, primary_key=True, index=True)
    jam = Column(String)
    tanggal = Column(String)