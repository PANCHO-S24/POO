import csv
from claseEmpleado_contratado import EmpleadoContratado
from claseEmpleado_externo import EmpleadoExterno
from claseEmpleado_planta import EmpleadoPlanta
from claseColeccion import ColeccionEmpleados

def cargar_empleados(archivo, funcion_crear_empleado, coleccion):
    with open(archivo, 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            empleado = funcion_crear_empleado(row)
            coleccion.agregar_empleado(empleado)

def main():
    coleccion = ColeccionEmpleados(10)

    cargar_empleados('planta.csv',EmpleadoPlanta,coleccion)
    cargar_empleados('contratados.csv', EmpleadoContratado,coleccion)
    cargar_empleados('externos.csv', EmpleadoExterno,coleccion)

    print("Listado de empleados:")
    coleccion.listar_empleados()

    print("\nSueldo total de empleados de planta:")
    print(coleccion.calcular_sueldo_por_tipo(EmpleadoPlanta))

    print("\nSueldo total de empleados contratados:")
    print(coleccion.calcular_sueldo_por_tipo(EmpleadoContratado))

    print("\nSueldo total de empleados externos:")
    print(coleccion.calcular_sueldo_por_tipo(EmpleadoExterno))

    print("\nEmpleado con mayor sueldo:")
    empleado_mayor_sueldo = coleccion.obtener_empleado_con_mayor_sueldo()
    print(f"DNI: {empleado_mayor_sueldo.get_dni()}, Nombre: {empleado_mayor_sueldo.get_nombre()}, Sueldo: {empleado_mayor_sueldo.calcular_sueldo()}")

    # Registrar horas
    dni = input("\nIngrese el DNI del empleado para registrar horas trabajadas: ")
    horas = int(input("Ingrese la cantidad de horas trabajadas: "))
    coleccion.registrar_horas(dni, horas)

if __name__ == '__main__':
    main()