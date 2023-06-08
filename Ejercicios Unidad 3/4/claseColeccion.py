import numpy as np
from claseEmpleado import Empleado
from claseEmpleado_planta import EmpleadoPlanta
from claseEmpleado_contratado import EmpleadoContratado
from claseEmpleado_externo import EmpleadoExterno

class ColeccionEmpleados:
    def __init__(self, max_empleados):
        self.__empleados = []
        self.__max_empleados = max_empleados

    def agregar_empleado(self,empleado):
        if len(self.__empleados) == self.__max_empleados:
            print("No se pueden agregar más empleados.")
        else:
            self.__empleados.append(empleado)
    
    def registrar_horas(self,dni,horas_trabajdas):
        empleado = self.buscar_empleado(dni)
        if empleado is not None:
            if isinstance(empleado,EmpleadoContratado):
                empleado.registrar_horas(horas_trabajdas)
            else: 
                print(f"el empleado con Dni {dni} no es un empleado contratado")
        else:
            print(f"No se encontro ningun empleado con dni {dni}")
    
    def total_tarea(self, tarea):
        total = 0
        for empleado in self.__empleados:
            if isinstance(empleado, EmpleadoExterno) and empleado.get_tarea() == tarea and not empleado.finalizo_tarea():
                total += empleado.calcular_pago()
        print(f"El monto a pagar por la tarea {tarea} es de ${total}.")
        
    def listar_empleados(self):
        i = 0
        while i < len(self.__empleados):
            empleado = self.__empleados[i]
            if empleado is not None:
                print(f"DNI: {empleado.get_dni()}, Nombre: {empleado.get_nombre()}, Sueldo: {empleado.calcular_sueldo()}")
            i += 1