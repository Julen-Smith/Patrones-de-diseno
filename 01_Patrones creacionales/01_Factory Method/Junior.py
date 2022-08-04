from Programador import *
from Front import *

class Programador_junior (Programador):
	
	tipo_de_programador = ""

	def __init__(self):
		tipo_de_programador = "Junior"
		self.Programando()
		pass

	def Programando(self)-> Programa:
		speech = "Junior crea un programa usando la clase padre {Programador}"
		super(Programador_junior,self).crear_un_programa(speech)
		print ("El programador"+ self.tipo_de_programador + " esta programando.")
		return Front().ha_programado()

