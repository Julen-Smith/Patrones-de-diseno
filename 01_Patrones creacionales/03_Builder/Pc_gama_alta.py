from ConstructorDePcs import *


class PcGamaAlta(ConstructorDePcs):
    modulos_de_ram = "Ram No contratado."
    disco_duro = "Disco duro No contratado."
    procesador = "Procesador No contratado."
    grafica = "Grafica No contratado."
    placa_base = "Placa base No contratado."
    tipo_producto = "none"

    def crear_modulos_de_ram(self) -> any:
        self.modulos_de_ram = "Se han creado modulos de ram a 3600mhz"
        return self

    def crear_discos_duros(self) -> any:
        self.disco_duro = "Se han creado un m2 de 5TB"
        return self

    def crear_procesador(self) -> any:
        self.procesador = "Se ha creado un Ryzen Threadripper"
        return self

    def crear_tarjeta_gráfica(self) -> any:
        self.grafica = "Se ha creado una RTX 3060"
        return self

    def crear_placa_base(self) -> any:
        self.placa_base = "Se han creado una Aorus Ultra Persistance AOX5400"
        return self

    def print_specs(self):
        print("Especificaciones de pc gama alta")
        print(self.placa_base + "\n" + self.procesador + "\n" + self.disco_duro + "\n" + self.modulos_de_ram + "\n" + self.grafica)
        print("\n")

    def __init__(self):
        pass