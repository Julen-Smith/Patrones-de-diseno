import Fabrica_de_ejercicios


class Estudiante(Fabrica_de_ejercicios):

    def __init__(self, name, subject, iq):
        self.name = name
        self.subject = subject
        self.iq = iq
