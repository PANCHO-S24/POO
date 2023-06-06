class Helado:
    __cantidadpedidos = 0
    __idhelado = None
    __gramos = None
    __precio = None
    __sabores = list()

    def __init__(self, gramos, precio,sabores=None):
        self.__gramos = gramos
        self.__precio = precio
        self.__idhelado = Helado.__cantidadpedidos
        # Incrementar el atributo class __cantidadpedidos
        Helado.__cantidadpedidos += 1
        # Agregue los sabores al atributo __sabores si sabores es distinto a  Ninguno
        if sabores != None:
            self.addSabores(sabores,1)
    
    # Método para agregar sabores al atributo __sabores
    def addSabores(self,sabores,cantidad):
        for i in range(cantidad):
            self.__sabores.append(sabores)

    def cerrarPedido(self):
        print("------------------------------------------------------------------------")
        print("Pedido numero: ",self.__idhelado)
        print("Nombre del helado: ",self.getNombreSabor())
        print("Gramos: ",self.__gramos)
        print("Precio: ",self.__precio)
        print("------------------------------------------------------------------------")
    
    # Método para obtener el nombre del primer sabor en el atributo __sabores
    def getNombreSabor(self):
        return self.__sabores
    
    def item(self):
        return list(self.__dict__.items())