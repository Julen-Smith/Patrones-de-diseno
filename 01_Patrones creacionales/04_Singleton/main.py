from Singleton import *

if __name__ == '__main__':

    s1 = Singleton()
    s2 = Singleton()
    s3 = Singleton()
    s4 = Singleton()

    print("Instancia 1 : " + str(id(s1)))
    print("Instancia 2 : " + str(id(s2)))
    print("Instancia 3 : " + str(id(s3)))
    print("Instancia 4 : " + str(id(s4)))
