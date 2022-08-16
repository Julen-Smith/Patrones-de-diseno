from Ejercicios_de_matematicas import *
from Ejercicios_de_programacion import *


class Estudiante42(EjerciciosDeMatemáticas, EjerciciosDeProgramación):

    def __init__(self, name, subject, iq, constancia):
        self.name = name
        self.subject = subject
        self.iq = iq
        self.constancia = constancia

    def acción_estudiantil(self, estudiante):
        if self.subject == "Matemáticas":
            EjerciciosDeMatemáticas(estudiante)
        elif self.subject == "Programación":
            EjerciciosDeProgramación(estudiante)
        else:
            print("El estudiante no ha realizado nada, otro año sin ser productivo.")

