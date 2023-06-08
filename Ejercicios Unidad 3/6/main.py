from claseListaVehiculo import ListaVehiculos
from claseVehiculo import Vehiculo

def main():
    lista_vehiculos = ListaVehiculos()
    lista_vehiculos.cargar_desde_archivo("vehiculos.json")

    while True:
        print("Menú de opciones:")
        print("1- Insertar un vehículo en la colección en una posición determinada ")
        print("2- Agregar un vehículo a la colección (funcionando)")
        print("3- Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición ")
        opcion = int(input(" Ingrese el número de la opción que desea realizar: "))

        if opcion == 1:
            # Insertar un vehículo
            modelo = input("Ingrese el modelo del vehículo: ")
            puertas = int(input("Ingrese la cantidad de puertas: "))
            color = input("Ingrese el color del vehículo: ")
            precio_base = float(input("Ingrese el precio base del vehículo: "))
            vehiculo = Vehiculo(modelo, puertas, color, precio_base)
            posicion = int(input("Ingrese la posición donde desea insertar el vehículo: "))
            usado = input("¿El vehículo es usado? (S/N): ")
            if usado.upper() == "S":
                patente = input("Ingrese la patente del vehículo: ")
                marca = input("Ingrese la marca del vehículo: ")
                anio = int(input("Ingrese el año del vehículo: "))
                kilometraje = float(input("Ingrese el kilometraje del vehículo: "))
                vehiculo.get_usado(patente, marca, anio, kilometraje)
            lista_vehiculos.insertar(vehiculo, posicion)
        elif opcion == 2:
            # Agregar un vehículo
            modelo = input("Ingrese el modelo del vehículo: ")
            puertas = int(input("Ingrese la cantidad de puertas: "))
            color = input("Ingrese el color del vehículo: ")
            precio_base = float(input("Ingrese el precio base del vehículo: "))
            vehiculo = Vehiculo(modelo, puertas, color, precio_base)
            lista_vehiculos.agregar(vehiculo)
            lista_vehiculos.mostrar_datos()
        elif opcion == 3:
            # Mostrar información de un vehículo por posición
            posicion = int(input("Ingrese la posición del vehículo que desea ver: "))
            print(lista_vehiculos.mostrar_informacion(posicion))

if __name__ == "__main__":
    main()