from ConstructorDePcs import *


class PcGamaBaja(ConstructorDePcs):
    modulos_de_ram = "Ram No contratado."
    disco_duro = "Disco duro No contratado."
    procesador = "Procesador No contratado."
    grafica = "Grafica No contratado."
    placa_base = "Placa base No contratado."
    tipo_producto = "none"

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

    def print_specs(self):
        print("Especificaciones de pc gama baja")
        print(self.placa_base + "\n" + self.procesador + "\n" + self.disco_duro + "\n" + self.modulos_de_ram + "\n" + self.grafica)
        print("\n")

    def __init__(self):
        pass
