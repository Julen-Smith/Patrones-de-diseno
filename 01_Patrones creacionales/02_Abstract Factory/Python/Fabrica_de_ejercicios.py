from abc import ABC, abstractmethod


@abstractmethod
class FábricaDeEjercicios(ABC):

    @abstractmethod
    def búsqueda_de_información(self, estudiante) -> any:
        print("Impl. random de búsqueda")

    @abstractmethod
    def planificación(self, estudiante) -> any:
        print("Impl. random de planificación")

    @abstractmethod
    def trabajo(self, estudiante) -> any:
        print("Impl. random de trabajo")

    @abstractmethod
    def examen(self, estudiante) -> any:
        print("Impl. random de examen")



