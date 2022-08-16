from Programador import *
from Back import *


class Programador_senior (Programador):

	tipo_de_programador = ""

	def __init__(self):
		self.tipo_de_programador = "Senior"
		self.Programando()
		pass

	def Programando(self) -> any:
		speech = "Senior crea un programa usando la clase padre {Programador}"
		super(Programador_senior, self).crear_un_programa(speech)
		print("El programador" + self.tipo_de_programador + " esta programando.")
		return Back().ha_programado()

