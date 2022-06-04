# Import libraries
from fastapi import Depends, FastAPI
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
# from classes.DaftarFavorit import
# from classes.DaftarHitam import
# from classes.Histori import 
from classes.KoleksiSaya import KoleksiSaya
from classes.DaftarFavorit import DaftarFavorit
from classes.DaftarHitam import DaftarHitam
# from classes.Resto import
# from classes.Review import 
# from classes.User import

# Initiate app and router
app = FastAPI()
router = InferringRouter()

@cbv(router)
class App:
    DH = DaftarHitam(1, "Foo", 15.40, '11/11/2021')
    DF = DaftarFavorit(1, "Bar", 8.40, '05/03/2018')
    list_hitam = Depends(DH.getAll())
    list_favorit = Depends(DF.getAll())

    @router.get("/profil-daftarhitam")
    def getDaftarHitam(self):
        return self.list_hitam

    @router.get("/profil-koleksifavorit")
    def getDaftarFavorit(self):
        return self.list_favorit

app.include_router(router)

