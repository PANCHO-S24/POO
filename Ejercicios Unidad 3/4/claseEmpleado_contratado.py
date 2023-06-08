from claseEmpleado import Empleado

class EmpleadoContratado(Empleado):
    __fecha_inicio = 'str'
    __fecha_fin = 'str'
    __horas_trabajadas = 'int'
    __valor_hora = 'float'
    
    def __init__(self, dni, nombre, direccion, telefono, fecha_inicio, fecha_fin, horas_trabajadas, valor_hora):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__horas_trabajadas = horas_trabajadas
        self.__valor_hora = valor_hora
    
    def get_fecha_inicio(self):
        return self.__fecha_inicio
    def get_fecha_fin(self):
        return self.__fecha_fin
    def get_horas_trabajadas(self):
        return self.__horas_trabajadas
    def get_valor_hora(self):
        return self.__valor_hora

    def calcular_sueldo(self):
        return self.__horas_trabajadas * self.__valor_hora
        