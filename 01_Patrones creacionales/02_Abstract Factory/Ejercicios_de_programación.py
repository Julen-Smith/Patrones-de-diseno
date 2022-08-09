from Estudiante import *
from Fabrica_de_ejercicios import *


class EjerciciosDeProgramación(FábricaDeEjercicios):

    def __init__(self, estudiante):
        print("Se han comenzado a realizar los ejercicios de Programación")
        self.búsqueda_de_información(estudiante)
        self.planificación(estudiante)
        self.trabajo(estudiante)
        self.examen(estudiante)

    def búsqueda_de_información(self, estudiante) -> any:
        print(estudiante.name + " ha empezado con la búsqueda de información en Stack overflow")

    def planificación(self, estudiante) -> any:
        print(estudiante.name + " ha empezado con la planificación de la Minishell")

    def trabajo(self, estudiante) -> any:
        if estudiante.constancia < 50:
            print("El trabajo realizado en el ejercicio de programación ha sido lamentable.")
        else:
            print("El trabajo realizado en el ejercicio de programación ha sido un éxito!")

    def examen(self, estudiante):
        if estudiante.iq < 100:
            print("El estudiante no ha aprobado el examRank09")
        else:
            print("El estudiante ha aprobado el examRank09")

