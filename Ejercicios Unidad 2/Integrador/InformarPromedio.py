import ManejadorAlumnos
import ManejadorMaterias

def informarPromedio(arreglo,lista):
    Dni = str(input("Ingrese el dni de un alumno:"))
    DniABuscar=arreglo.compararDNI(Dni)
    if DniABuscar != "Error":
        lista.buscarNotas(DniABuscar)
    else:
        print(" dni no encontrado")
