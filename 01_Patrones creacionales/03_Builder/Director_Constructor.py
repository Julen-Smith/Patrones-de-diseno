from ConstructorDePcs import *
from Pc_gama_alta import *
from Pc_gama_baja import *
from Pc_gama_media import *


class DirectorConstructor:

    pc = None
    def cambiar_tipo_producto(self, producto):
        if producto == "Alta01":
            self.pc = PcGamaAlta()
            self.pc.tipo_producto = "Alta01"
        elif producto == "Alta02":
            self.pc = PcGamaAlta()
            self.pc.tipo_producto = "Alta02"
        elif producto == "Media01":
            self.pc = PcGamaMedia()
            self.pc.tipo_producto = "Media01"
        elif producto == "Media02":
            self.pc = PcGamaMedia()
            self.pc.tipo_producto = "Media02"
        elif producto == "Baja01":
            self.pc = PcGamaBaja()
            self.pc.tipo_producto = "Baja01"
        elif producto == "Baja02":
            self.pc = PcGamaBaja()
            self.pc.tipo_producto = "Baja02"

    def build(self):
        if self.pc.tipo_producto == "none":
            pass
        if self.pc.tipo_producto == "Alta02" :
            self.pc.crear_discos_duros().crear_modulos_de_ram().crear_procesador().crear_tarjeta_gráfica()\
                .crear_placa_base()
        elif self.pc.tipo_producto == "Alta01":
            self.pc.crear_discos_duros().crear_modulos_de_ram().crear_procesador().crear_tarjeta_gráfica()
        if self.pc.tipo_producto == "Media02":
            self.pc.crear_discos_duros().crear_modulos_de_ram().crear_tarjeta_gráfica()\
                .crear_placa_base()
        elif self.pc.tipo_producto == "Media01":
            self.pc.crear_discos_duros().crear_modulos_de_ram().crear_procesador().crear_tarjeta_gráfica()
        if self.pc.tipo_producto == "Baja02":
            self.pc.crear_discos_duros().crear_modulos_de_ram().crear_procesador().crear_tarjeta_gráfica()\
                .crear_placa_base()
        elif self.pc.tipo_producto == "Baja01":
            self.pc.crear_discos_duros().crear_modulos_de_ram().crear_procesador().crear_tarjeta_gráfica()
        self.pc.print_specs()
        pass

    def __init__(self):
        pass
