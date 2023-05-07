import csv
from clase import Email

class ManejadorCorreo:
    self.__listacorreo= []

    def __init__(self):
           self.__listacorreo= []

    def agregarCorreos(self, uncorreo):
        self.__listacorreo.append(uncorreo)
    
    def testCorreos(self):
        archivo=open('correosElectronicos1.csv')
        reader= csv.reader(archivo,delimiter =',')
        for fila in reader:
            idcuenta= int(fila[0])
            dominio = fila[1]
            tipodom = int(fila[2])
        uncorreo=Email(idcuenta, dominio, tipodom)
        self.__listacorreo.append(uncorreo)
        archivo.close()