from Estudiante import *
from Fabrica_de_ejercicios import *


class EjerciciosDeMatemáticas(FábricaDeEjercicios):

    def búsqueda_de_información(self, estudiante) -> any:
        print(estudiante.name + " ha empezado con la búsqueda de información")

    def planificación(self, estudiante) -> any:
        print(estudiante.name + " ha empezado con la planificación")

    def trabajo(self, estudiante) -> any:
        if estudiante.constancia < 50:
            print("El trabajo realizado en el ejercicio de matemáticas ha sido lamentable.")
        else:
            print("El trabajo realizado en el ejercicio de matemática ha sido un éxito!")

    def examen(self, estudiante) -> any:
        if estudiante.iq < 100:
            print("El estudiante no ha aprobado el examen")
        else:
            print("El estudiante ha aprobado")

    def __init__(self, estudiante):
        print("Se han comenzado a realizar los ejercicios de matemáticas")
        self.búsqueda_de_información(estudiante)
        self.planificación(estudiante)
        self.trabajo(estudiante)
        self.examen(estudiante)
