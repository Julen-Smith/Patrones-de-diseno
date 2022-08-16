from Robot import Robot
from musical_IA import *


# En este ejemplo tenemos dos Ias malvadas que se degeneran pasado un tiempo.
# Un robot heredará la clase Ia y se degenerará con el tiempo, como necesitamos un robot músico durante un tiempo
# cuando se estropee clonaremos el objeto Robot y heredará otra IA de nuevo,
# de manera que tendremos dos Robots uno totalmente Corrupto que estará con ganas de matar (Pero se le quiere)
# y otro que estará cumpliendo las funciones del anterior , al menos, de momento con el mismo nombre marca y en resumen
# todos los atributos que tenía el robot anterior.


if __name__ == '__main__':
    # Generamos el robot
    robot = Robot("Wall-e", "Model : T2.0", "Cool", "Python")
    print("Dirección de memoria robot es : " + str(robot))
    # Generamos la IA
    ia = MusicIa()
    robot.add_ia(ia)
    robot.ia.generate_ia()
    robot.ia.generate_ia()
    robot.ia.generate_ia()
    robot.ia.generate_ia()
    robot.ia.degenerate_ia()
    robot.ia.degenerate_ia()
    robot.ia.degenerate_ia()
    robot.ia.degenerate_ia()
    robot.ia.degenerate_ia()
    robot.ia.degenerate_ia()
    robot_clone = robot.clone()
    print("Dirección de memoria clon es : " + str(robot_clone))
    robot_clone.kill_human()

# Conclusión se crean los robots pero a la hora de clonar el principal al introducirle
# la IA del primero, se quedan dos objetos identicos con distintas funcionalidades