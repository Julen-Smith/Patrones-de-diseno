from __future__ import annotations
from abc import ABC,abstractmethod
from Programa import *

class Programador(ABC):

	@abstractmethod
	def Programando(self):
		#print ("Esta es una implementación por defecto de un Programador")
		pass

	def crear_un_programa(self, string) -> str:
		print (string)
		return string 