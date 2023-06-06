from collections import Counter
from ClaseSabor import Sabor
from ClaseHelado import Helado
from datetime import datetime
from ManejaSabores import manejadorSabor

class manejadorHelado:
    __helados = []

    def __init__(self):
        self.__helados = []
    
    # Agregar el objeto helado al atributo __listaHelados
    def registrarHelado(self, helado):
        self.__helados.append(helado)

    def cerrarPedido(self):
        print("------------------------------------------------------------------------")
        print("Pedido cerrado a las", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        for helado in self.__helados:
            helado.cerrarPedido() # Llama al método cerrarPedido() de cada objeto helado en el atributo __listaHelados

    def getListaHelados(self):
        return self.__helados # Devuelve el atributo __listaHelados
    
    def obtenersabormaspedido(self):
        contador_sabores = Counter()
        idx_helado = 0
        while idx_helado < len(self.__helados):
            helado = self.__helados[idx_helado]
            idx_sabor = 0
            while idx_sabor < len(helado._Helados__sabores):
                sabor = helado._Helados_sabores[idx_sabor]
                contador_sabores[sabor._Sabor__idSabor] += 1
                idx_sabor += 1
            idx_helado += 1

        top_5_sabores = contador_sabores.most_common(5)

        print("Los 5 sabores más pedidos son:")
        for sabor, cantidad in top_5_sabores:
            print(f"ID del sabor: {sabor}, cantidad de pedidos: {cantidad}")
    
    def gramos_vendidos(self,num_sabor):
        gramosvendidos = 0
        id_helado= 0
        while id_helado <len (self.__helados):
            helado = self.__helados[id_helado]
            id_sabor = 0
            while id_sabor < len(helado._Helados__sabores):
                sabor=helado._Helados__sabores[id_sabor]
                if sabor._Sabor__idSabor == num_sabor:
                    gramosvendidos +=helado._Helado__gramos
                    break
                id_sabor +=1
            id_helado +=1
        print(f"Se vendieron aproximadamente {gramos_vendidos} gramos del sabor {num_sabor}")   