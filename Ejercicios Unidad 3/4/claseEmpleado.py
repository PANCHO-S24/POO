class Empleado:
    __dni='int'
    __nombre='str'
    __direccion='str'
    __telefono='int'
    
    def __init__(self, dni, nombre, direccion, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
    
    def get_dni(self):
        return self.__dni
    def get_nombre(self):
        return self.__nombre
    def get_direccion(self):
        return self.__direccion
    def get_telefono(self):
        return self.__telefono
    
    def set_dni(self,dni):
        self.__dni = dni