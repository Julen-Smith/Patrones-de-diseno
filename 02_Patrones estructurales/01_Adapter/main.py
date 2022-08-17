from Cargador import *
from Cargador_Adapter import cargadorAdapter


if __name__ == '__main__':
    carga = cargador()
    adapter = cargadorAdapter(carga)
    adapter.adapter()
    print("Voy a España")
    adapter.pais = "España"
    adapter.adapter()
    print("Voy a Inglaterra")
    adapter.pais = "Inglaterra"
    adapter.adapter()
