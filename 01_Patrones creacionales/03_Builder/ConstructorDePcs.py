from abc import ABC, abstractmethod


class ConstructorDePcs(ABC):

    @abstractmethod
    def crear_modulos_de_ram(self):
        print("Impl por defecto de la creación de rams")

    @abstractmethod
    def crear_discos_duros(self):
        print("Impl por defecto de la creación de discos duros")

    @abstractmethod
    def crear_procesador(self):
        print("Impl por defecto de la creación del procesador")

    @abstractmethod
    def crear_tarjeta_gráfica(self):
        print("Impl por defecto de la creación de la tarjeta grafica")

    @abstractmethod
    def crear_placa_base(self):
        print("Impl por defecto de la creación de la placa base")


