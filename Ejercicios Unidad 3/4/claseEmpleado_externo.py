from claseEmpleado import Empleado

class EmpleadoExterno(Empleado):
    __tarea= 'str'
    __fecha_inicio = 'str'
    __fecha_fin = 'str'
    __monto_viatico = 'float'
    __costo_obra = 'float'
    __monto_seguro = 'float'
    
    def __init__(self, dni, nombre, direccion, telefono, tarea, fecha_inicio, fecha_fin, monto_viatico, costo_obra, monto_seguro):
       super().__init__(dni, nombre, direccion, telefono)
       self.__tarea = tarea
       self.__fecha_inicio = fecha_inicio
       self.__fecha_fin = fecha_fin
       self.__monto_viatico = monto_viatico
       self.__costo_obra = costo_obra
       self.__monto_seguro = monto_seguro
    def get_tarea(self):
        return self.__tarea
    def get_fecha_inicio(self):
        return self.__fecha_inicio
    def get_fecha_fin(self):
        return self.__fecha_fin
    def get_monto_viatico(self):
        return self.__monto_viatico
    def get_costo_obra(self):
        return self.__costo_obra
    def get_monto_seguro(self):
        return self.__monto_seguro
    
    def calcular_sueldo(self):
        return self.__costo_obra - (self.__monto_viatico + self.__monto_seguro)