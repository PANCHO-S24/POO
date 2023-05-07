from clases import PlanAhorro
from generalista import Planes
import csv

if __name__ == '__main__':
    lista = Planes()

    while True:
        print("\nMenu de opciones: ")
        print("1--Mostrar lista cargada")
        print("2--Actualizar valores de planes")
        print("3--mostrar datos del vehículo cuyo valor de la cuota sea inferior al valor dado")
        print("4--Importe de cuotas de cada plan:")
        print("5--Modificar cuotas para licitar:")
        print("0--Salir del menu:")
        opcion = input("\nIngrese una opcion: ")

        if opcion == "1":
            print("\n----Datos de la lista----\n")
            lista.test()
        else:
            if opcion == "2":
                lista.actualizar()
            else:
                if opcion == "3":
                    cuotas = input("Ingrese la cantidad de cuotas: ")
                    lista.CantCuotas(cuotas)
                else:
                    if opcion == "4":
                        lista.importecuota()  
                    else:
                        if opcion == "5":
                            lista.actualizarCuotasLicitar()
                        else:
                            if opcion == "0":
                                break
                            else:
                                print("Opcion no valida")