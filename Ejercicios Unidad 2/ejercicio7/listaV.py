from claseV import Viajerofrecuente
import csv
class manejadorL:
    __listaviajeros= []

    def __init__(self):
          self.__listaviajeros = []
    
    def  testViajero(self):
            archivo= open("ViajeroFrecuente.csv")
            reader= csv.reader(archivo,delimiter=';')
            for fila in reader:
                num_viajero = fila[0]
                dni = fila[1]
                nombre = fila[2]
                apellido = fila[3]
                millas_acum= int(fila[4])
                unViajero= Viajerofrecuente(num_viajero,dni, nombre, apellido, millas_acum)
                self.__listaviajeros.append(unViajero)
            archivo.close()
               
            i=0
            while (i<len(self.__listaviajeros)):
                Viajero = self.__listaviajeros[i].mostrardatos()
                print("viajero : ",Viajero)
            i= i+1
    def mayorMillas(self):
        viajero_mayor_millas = max(self.__listaviajeros) #el max va relacionadon el metodo __gt__, por eso se ejecuta sin necesidad de llamarlo aca
        print(viajero_mayor_millas.datosMayorMillas())
