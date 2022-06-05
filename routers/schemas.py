from pydantic import BaseModel

class KoleksiFavorit(BaseModel):
    status: str
    jam: str
    tanggal: str

class DaftarHitam(BaseModel):
    status: str
    jam: str
    tanggal: str