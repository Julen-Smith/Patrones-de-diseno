class SingletonMeta(type):

    #CLS hace referencia a la propia clase THISCLASS
    #Init hace referencia a la creación del objeto (1 vez por objeto creado), call se ejecuta siempre y cuando la instancia sea llamada
    #La clase type fuerza a recibir por parametro la clase de la que se va a hacer meta
    _instancias = {}

    def __call__(cls):
        if cls not in cls._instancias:
            instance = super().__call__()
            cls._instancias[cls] = instance
        return cls._instancias[cls]
