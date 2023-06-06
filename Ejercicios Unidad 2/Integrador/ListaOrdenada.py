import ManejadorAlumnos
import ManejadorMaterias

def MostrarLisOrdenado(arreglo, lista):
    ListPorApell = arreglo.obtenerListOrdenadaApelldo()
    ListPorApell.sort()
    print("Lista ordenada de alumnos Alfabeticamente: ")
    for i in range(len(ListPorApell)):
        print(ListPorApell[i])
