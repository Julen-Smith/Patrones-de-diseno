from __future__ import annotations
from abc import ABC,abstractmethod


class Programa (ABC):
	
	def __init__(self):
		pass

	@abstractmethod
	def ha_programado(self) -> any:
		pass
