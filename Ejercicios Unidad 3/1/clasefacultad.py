class Facultad:
    __codigo : int  # al definirse con : se define como variable de clase
    __nombre : str
    __direccion : str
    __localidad : str
    __telefono :str
    __carreras: list
    
    def __init__(self,codigo,nombre,direccion,localidad,telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion= direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carreras = []
    
    def agregar_carrera(self,carrera):
        self.__carreras.append(carrera)

    def getNombref(self):
        return self.__nombre
    def getCodigof(self):
        return self.__codigo
    def getDirecccion(self):
        return self.__direccion
    def getLocalidad(self):
        return self.__localidad
    def getTelefono(self):
        return self.__nombre
    def get_Carreras(self):
        return self.__carreras
    def get_Carrera(self,i):
        return self.__carreras[i]

    def __str__(self):
        return f'{self.__nombre}'