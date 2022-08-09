from Fabrica_de_ejercicios import *


class ejerciciosDeMatemáticas(FábricaDeEjercicios):

    def búsqueda_de_información(self, estudiante) -> any:
        print(estudiante.name + "ha empezado con la búsqueda de información")

    def planificación(self, estudiante) -> any:
        pass

    def trabajo(self, estudiante) -> any:
        pass

    def examen(self, estudiante) -> any:
        pass

    def __init__(self, estudiante):
        estudiante = estudiante
        self.búsqueda_de_información(estudiante)
