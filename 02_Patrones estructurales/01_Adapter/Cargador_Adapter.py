from Cargador import cargador
from Enchufe_espanol import *
from Enchufe_ingles import *


class cargadorAdapter:

    pais = ""
    carga: cargador

    def __init__(self, carga: cargador):
        self.carga = carga

    def definir_pais(self, pais):
        self.pais = pais

    def adapter(self):
        if self.pais == "España":
            return EnchufeEspanol()
        elif self.pais == "Inglaterra":
            return EnchufeIngles()
        else:
            print("No se a que país voy")
