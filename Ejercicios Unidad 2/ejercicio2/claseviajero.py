

class Viajerofrecuente:
    __num_viajero :int
    __dni :str
    __nombre :str
    __apellido : str
    __millas_acum: int

    def  __init__(self,num_viajero,dni,nombre,apellido,millas_acum):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum
    
    def retorna_millas(self):
        return self.__millas_acum

    def acumularMillas(self, Mrecorridas):
        total = self.__millas_acum + Mrecorridas
        print("Valor actualizado: ", total )

    def canjearMillas(self,CMillas):
        if self.__millas_acum >= CMillas:
            print(" Las millas se pueden canjear ") 
        else: 
            print("las millas no pueden canjearse")
            print("tienes :",self.__millas_acum)

    def mostrarDatos(self):
        print("Nombre viajero :",self.__nombre)
    
    def getNombre(self):
        return self.__nombre + self.__apellido
