from IA import Ia


class Robot:

    ia: Ia = None
    corrupted = False

    def __init__(self, name, model, style, language):
        self.name = name
        self.model = model
        self.style = style
        self.language = language
        print("El robot ha sido generado")

    def add_ia(self, ia):
        if not self.ia:
            print("El robot no tiene ia")
        self.ia = ia

    def kill_human(self):
        if not self.ia:
            print("Friendly Robot :)")
        else:
            print("You will die")
            self.ia.kill_human()
            self.corrupted = True

    def clone(self):
        if self.corrupted:
            print("El robot está roto, no se clonará")
        else:
            return Robot(self.name, self.model, self.style, self.language)

