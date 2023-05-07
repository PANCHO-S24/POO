from typing import Any

class Ventana:
    __titulo = " "
    __valorX1= " "
    __valorY1= " "
    __valorX2= " "
    __valorY2= " "

    def __init__ (self,titulo,valorX1= 0,valorY1= 0,valorX2= 500, valorY2= 500):
        self.__titulo= titulo
        self.__valorX1= max(0,valorX1)
        self.__valorY1= max(0,valorY1)
        self.__valorX2= min(500,valorX2)
        self.__valorY2= min(500,valorY2)

    def getTitulo(self):
        return self.__titulo
    def valorX1(self):
        return self.__valorX1
    def valorY1(self):
        return self.__valorY1
    def valorX2(self):
        return self.__valorX2
    def valorY2(self):
        return self.__valorY2
    
    def alto(self):
        return ({self.__valorY1} - {self.__valorY2})
    
    def ancho(self):
        return ({self.__valorX2} - {self.__valorX1})
    

    def mostrar(self):
        print ('ventana en :', {self.__titulo}, {self.__valorX1}, {self.__valorY1}, {self.__valorX2}, {self.__valorY2})

    def moverDerecha(self, valor =1):
        self.__valorX1 += valor
        self.__valorX2 += valor
    
    def moverIzquierda(self, valor):
        self.__valorX1 -= valor
        self.__valorX2 -= valor
   
    def bajar(self, valorY1=1, valorY2=1):
        self.__valorY1 -= valorY1
        self.__valorY2 -= valorY2
    
    def subir(self, valorY1=1, valorY2=1):
        self.__valorY1 += valorY1
        self.__valorY2 += valorY2  
