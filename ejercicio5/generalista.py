from clases import PlanAhorro
import csv

class Planes:
    __listaPlanes = []
    def __init__(self):
        self.__listaPlanes = []
    
    def agregaplanes(self,unPlan):
        self.__listaPlanes.append(unPlan)
    
    def test(self):
        archivo = open('planes.csv')
        reader = csv.reader(archivo,delimiter = ";")
        for fila in reader:
            cod =str(fila[0])
            mod = (fila[1])
            ver =(fila[2])
            pre = (fila[3])
            cc = (fila[4])
            cl = str(fila[5])
            unPlan= PlanAhorro(cod,mod,ver,pre,cc,cl)
            self.agregaplanes(unPlan)
        i=0

        while(i<len(self.__listaPlanes)):
            plan= self.__listaPlanes[i].mostrarDatos()
            i+=1

    def actualizar(self):
        i = 0
        while(i<len(self.__listaPlanes)):
            nuevo_valor = input("\nIngrese el precio actualizado del plan: ") 
            print("---------------------------------")
            nuevoplan = self.__listaPlanes[i].actualizarValorAuto(nuevo_valor) 
            i+=1

    def CantCuotas(self,cuotas):
        i = 0
        while(i<len(self.__listaPlanes)):
            mdatos = self.__listaPlanes[i].mostrarPlanCuotaInf(cuotas)
            i+=1

    def importecuota(self):
        i = 0
        while(i<len(self.__listaPlanes)):
            importexcuota = self.__listaPlanes[i].importecuota()
            print("Importe de cuota de cada plan: ", importexcuota)
            i+=1
    def actualizarCuotasLicitar(self): 
        i = 0
        while(i<len(self.__listaPlanes)):
            nueva_cuota = input("\nActualize las cuotas: ") 
            print("---------------------------------")
            nuevoplan = self.__listaPlanes[i].modificarCuotas(nueva_cuota)
            print("---------------------------------")
            i+=1
        