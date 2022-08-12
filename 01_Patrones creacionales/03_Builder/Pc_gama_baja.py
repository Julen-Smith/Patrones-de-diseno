from ConstructorDePcs import *


class PcGamaBaja(ConstructorDePcs):
    modulos_de_ram = ""
    disco_duro = ""
    procesador = ""
    grafica = ""
    placa_base = ""

    def crear_modulos_de_ram(self) -> any:
        self.modulos_de_ram = "1 Modulo de ram a 1200mhz"
        return self

    def crear_discos_duros(self) -> any:
        self.disco_duro = "1 disco duro sólido de 500gb"
        return self

    def crear_procesador(self) -> any:
        self.disco_duro = "Intel core i3 9th"
        return self

    def crear_tarjeta_gráfica(self) -> any:
        self.grafica = "Intel hd graphics 3000"
        return self

    def crear_placa_base(self) -> any:
        self.placa_base = "Corsair Latitude 4500B"
        return self

    def __init__(self):
        pass
