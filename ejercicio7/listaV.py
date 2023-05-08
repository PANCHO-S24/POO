from claseV import Viajerofrecuente
import csv
class manejadorL:
    __listaviajeros= []

    def __init__(self):
          self.__listaviajeros = []

    def agregarViajero(self,unViajero):
          self.__listaviajeros.append(unViajero)  #agrega un viajero a la lista con el metodo append
    
    def  testViajero(self):
            archivo=open("ViajeroFrecuente.csv")
            reader=csv.reader(archivo,delimiter=',')
            for fila in reader:
                numero = int(fila[0])
                dni = fila[1]
                nombre = fila[2]
                apellido = fila[3]
                millas = int(fila[4])
                unViajero= Viajerofrecuente(num_viajero, dni, nombre, apellido, millas_acum)
                self.agregarViajero(unViajero)
            archivo.close()
               
            i=0
            while (i<len(self.__listaviajeros)):
                Viajero= self.__listaviajeros[i].getNombre
                print("viajero : ",Viajero)
            i+=1
    def mayorMillas(self):
        viajero_mayor_millas = max(self.__listaviajeros) #el max va relacionadon el metodo __gt__, por eso se ejecuta sin necesidad de llamarlo aca
        print(viajero_mayor_millas.datosMayorMillas())
