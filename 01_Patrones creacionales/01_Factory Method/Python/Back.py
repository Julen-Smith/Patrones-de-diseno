from __future__ import annotations
from Programa import *


class Back (Programa):

	def __init__(self):
		super().__init__()

	def ha_programado(self) -> str:
		print("Se ha realizado un programa en back")
		return "Se ha realizado un programa en back"
