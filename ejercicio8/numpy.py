import numpy as np

class conjunto:
    
    def __init__(self, datos):
        self.datos = np.array(datos, dtype=int) #pal conjunto de solo enteros 
        
    def __add__(self, other):
        
        nuevo_conjunto = Conjunto(set())
        
        for other in self.datos:
            nuevo_conjunto.datos.add(elemento)

        for elemento in other.datos:
            if elemento not in self.datos:
                nuevo_conjunto.datos.add(elemento)
        return nuevo_conjunto
        
    def __sub__(self, otro):
        return conjunto(np.setdiff(self.datos,otro.datos))  
    def __eq__(self, valor):
        return np.array_equal(self.datos,valor.datos) 