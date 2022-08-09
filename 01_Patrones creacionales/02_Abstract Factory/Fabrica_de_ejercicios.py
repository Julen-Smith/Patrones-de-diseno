from abc import abstractmethod


@abstractmethod
class FábricaDeEjercicios:

    @abstractmethod
    def búsqueda_de_información(self) -> any:
        print("Impl. random de búsqueda")

    @abstractmethod
    def planificación(self) -> any:
        print("Impl. random de planificación")

    @abstractmethod
    def trabajo(self) -> any:
        print("Impl. random de trabajo")

    @abstractmethod
    def examen(self) -> any:
        print("Impl. random de examen")



