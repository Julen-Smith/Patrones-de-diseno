from IA import Ia


class MusicIa(Ia):

    degenerated = 0
    corrupted = False

    def __init__(self):
        print("Ia ha sido generada")

    def generate_ia(self):
        print("Do Re Mi Fa Sol La Si Do")

    def degenerate_ia(self):
        if self.corrupted:
            self.kill_human()
            pass
        self.degenerated += 1
        print("Od Er Im Af Los Al Is Odddd")
        if self.degenerated == 5:
            self.corrupted = True

    def kill_human(self):
        print("M-Insane U-getting S-is I-ia. C1 + 3 is DO")
