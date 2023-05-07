
class PlanAhorro:
    codigo :str
    modelo : str
    version :str
    precio : float
    cant_cuotas :int
    cuotas_licitar :int
    
    def __init__(self, codigo, modelo, version,precio, cant_cuotas, cuotas_licitar):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__precio = precio
        self.__cant_cuotas = cant_cuotas
        self.__cuotas_licitar = cuotas_licitar

    def mostrarDatos(self):
        print("codigo del vehiculo:", self.__codigo)
        print("Modelo: ", self.__modelo)
        print("Version: ", self.__version)
        print("Precio: ", self.__precio)
        print("Cantidad de cuotas del plan: ", self.__cant_cuotas)
        print("Cant. cuotas para licitar el auto: ", self.__cuotas_licitar)
        print("--------------------------------------------------------")
        
    def actualizarValorAuto(self,nuevo_valor):
        print("Codigo del plan: ", self.__codigo)
        print("Modelo: ",self.__modelo)
        print("Version: ",self.__version)
        self.__precio = nuevo_valor
        print("nuevo precio :",self.__precio)

    def importecuota(self):
        return (int(self.__precio) * 0.10)
    
    def mostrarPlanCuotaInf(self,cuotas):
        if self.__cant_cuotas > cuotas:
            print(" codigo plan: ",self.__codigo)
            print(" modelo :",self.__modelo)
            print("version :",self.__version)
    
    def modificarCuotas(self, nueva_cuota):
        self.cuotas_licitar = nueva_cuota
        print("Se modifico la cantidad de cuotas: ")
