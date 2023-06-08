from claseEmpleado import Empleado

class EmpleadoPlanta(Empleado):
    __sueldo_basico= 'float'
    __antiguedad = 'int'

    def __init__(self, dni, nombre, direccion, telefono, sueldo_basico, antiguedad):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldo_basico = sueldo_basico
        self.__antiguedad = antiguedad
    
    def get_sueldo_basico(self):
        return self.__sueldo_basico
    
    def get_antiguedad(self):
        return self.__antiguedad
    
    def calcular_sueldo(self):
        return self.__sueldo_basico + (self.__sueldo_basico * 0.01 * self.__antiguedad)
