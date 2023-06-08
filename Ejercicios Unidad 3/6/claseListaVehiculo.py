from claseVehiculo import Vehiculo
import json
import datetime

class ListaVehiculos:
    def __init__(self):
        self.__vehiculos = []

    def __iter__(self):
        self.__indice = 0
        return self

    def __next__(self):
        if self.__indice < len(self.__vehiculos):
            vehiculo = self.vehiculos[self.__indice]
            self.__indice += 1
            return vehiculo
        else:
            raise StopIteration

    def insertar(self, vehiculo, posicion):
        self.__vehiculos.insert(posicion, vehiculo)

    def agregar(self, vehiculo):
        self.__vehiculos.append(vehiculo)

    def mostrar_informacion(self,posicion):
        return self.vehiculos[posicion]

    def mostrar_datos(self):
        for vehiculo in self.__vehiculos:
            print(vehiculo)

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as f:
                contenido = f.read()
                if contenido:
                    diccionarios_vehiculos = json.loads(contenido)
                    self.__vehiculos = self.diccionarios_a_vehiculos(diccionarios_vehiculos)
                else:
                    print(f"El archivo '{nombre_archivo}' está vacío. Se creará una nueva lista de vehículos.")
                    self.__vehiculos = []
        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no existe. Se creará una nueva lista de vehículos.")
            self.__vehiculos = []