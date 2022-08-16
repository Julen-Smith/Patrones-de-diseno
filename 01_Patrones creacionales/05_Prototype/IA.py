from abc import ABC, abstractmethod


class Ia(ABC):

    @abstractmethod
    def generate_ia(self):
        pass

    @abstractmethod
    def degenerate_ia(self):
        pass

    @abstractmethod
    def kill_human(self):
        pass
