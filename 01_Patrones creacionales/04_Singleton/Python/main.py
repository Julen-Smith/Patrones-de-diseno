from Singleton import *

if __name__ == '__main__':
    s1 = Singleton()
    print("Instancia 1 : " + str(id(s1)))
    s2 = Singleton()
    print("Instancia 2 : " + str(id(s2)))
    s3 = Singleton()
    print("Instancia 3 : " + str(id(s3)))
    s4 = Singleton()
    print("Instancia 4 : " + str(id(s4)))
