from ClaseSabor import Sabor
import csv

class manejadorSabor:
    __sabores = []
    def __init__(self):
        self.__sabores = []
    
    def cargarSabores(self):
        archivo = open("sabores.csv", encoding="utf-8")
        reader = csv.reader(archivo,delimiter=";")
        for i in reader:
            unSabor = Sabor(int(i[0]),i[1],i[2])
            self.__sabores.append(unSabor)
        print("Sabores cargados con exito!")
        print("-------------------------------------")
        archivo.close()
        
        i = 0
        
        while i<len(self.__sabores):
            self.__sabores[i].mostrarDatos()
            i+=1
        
    