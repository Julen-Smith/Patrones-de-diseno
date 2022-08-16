from __future__ import annotations
from Programa import *


class Programador(ABC):

	@abstractmethod
	def Programando(self):
		pass

	@staticmethod
	def crear_un_programa(string) -> str:
		print(string)
		return string
