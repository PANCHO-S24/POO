class Carrera:
    __codigo :int
    __nombrec :str
    __titulo : str 
    __duracion : str
    __tipo : str
    
    def __init__(self,codigo,nombre,titulo,duracion,tipo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__titulo = titulo
        self.__duracion = duracion
        self.__tipo = tipo
    
    def get_Codigoc(self):
        return self.__codigo
    def get_Nombrec(self):
        return self.__nombre
    def get_Duracion(self):
        return self.__duracion
    def get_Titulo(self):
        return self.__titulo
    def get_Tipo(self):
        return self.__tipo
    
    def __str__(self):
        return f'{self.__nombre} {self.__duracion}'
       
