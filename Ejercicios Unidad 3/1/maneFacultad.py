from clasefacultad import Facultad
from clasecarrera import Carrera
import csv

class ManejadorFacultad :
    __listafacultad :list
    
    def __init__(self):
        self.__listafacultad = []
    
    def get_facultad(self,i):
        return self.__listafacultad[i]
    
    def agregarfacultad(self,unaFacultad):
        self.__listafacultad.append(unaFacultad)
    
    def cargar_Facultad(self):
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo, delimiter = ';')
        indice = 0 
        for fila in reader:
            if int(fila[0]) == indice:
                unaCarrera = Carrera(int(fila[1]) ,fila[2] ,fila[3] ,fila[4],fila[5])
                self.__listafacultad[indice-1].agregar_carrera(unaCarrera)
            else:
                unaFacultad = Facultad(int(fila[0]),fila[1],fila[2],fila[3],fila[4])
                self.agregarfacultad(unaFacultad)
                indice+=1
        archivo.close()   

    def buscar_facultad(self,codigo):
        i=0
        bandera = False
        retorno = -1
        while not bandera and i<len(self.__listafacultad):
            if codigo == self.__listafacultad[i].getCodigof():
               bandera = True
               retorno = i
            i+=1
        return retorno 
    
    def buscar_carrera(self,nomb_carrera):
        band =False
        i=0
        while not band and i<len (self.__listafacultad):
            j=0
            while not band and j<len(self.__listafacultad):
                if self.__listafacultad[i].get_Carrera(j).get_Nombrec()== nomb_carrera:
                    band=True
                j+=1
            i+=1
        if not band:
            print("No se encontro la carrera")
        else:
             print(f"Codigo de la carrera:{self.__listafacultad[i-1].getCodigof()}.{self.__listafacultad[i-1].get_Carrera(j-1).get_Codigoc()}")
             print(f"{self.__listafacultad[i-1].getNombref()}{self.__listafacultad[i-1].getLocalidad()}")