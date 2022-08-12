from Pc_gama_baja import *
from Director_Constructor import *


if __name__ == '__main__':
    Builder = DirectorConstructor()
    Builder.cambiar_tipo_producto("Alta02")
    Builder.build()

    Builder.cambiar_tipo_producto("Alta01")
    Builder.build()

