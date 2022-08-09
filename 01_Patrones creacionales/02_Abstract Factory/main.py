from Estudiante import *

if __name__ == '__main__':
    print("Inicio del programa \n")
    EstudianteInteligente = Estudiante42("Peter", "Programación", 500, 20)
    EstudianteInteligente.acción_estudiantil(EstudianteInteligente)

    print("--------------------------")

    EstudianteConstante = Estudiante42("Jeffrey", "Matemáticas", 80, 200)
    EstudianteConstante.acción_estudiantil(EstudianteConstante)

    print("--------------------------")

    EstudianteNini = Estudiante42("BOB", "Jaja", 999, 999)
    EstudianteNini.acción_estudiantil(EstudianteNini)
