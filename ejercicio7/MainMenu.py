from listaV import manejadorL
from claseV import Viajerofrecuente
if __name__ == '__main__':
   lista = manejadorL()

while True:
      print("\nMenú de opciones:")
      print("\na--Mostrar Datos: ")
      print("b- Viajero con mayor millas acumuladas")
      print("c- Acumular Millas")
      print("d- Canjear Millas")
      print("e--Comparar millas acum: ")
      print("f- Salir")
      opcion = input("\nIngrese una opción: ")
      if opcion == "a":
            print("\n==Datos de la lista cargada==")
            lista.testViajero()
      else:
         if opcion == "b":
           lista.mayorMillas()
         else:
         
            if opcion == "c":
              vi = Viajerofrecuente(1,34455345,"martin","perez",1400)
              vi = vi + 100
              print(vi)    
            else:
                if opcion== "d":
                 vi2 = Viajerofrecuente(2,34478845,"tino","roblez",4500)
                 vi2 = vi2 - 100
                 print(vi2) 
                else:
                   if opcion== "e":
                    vi3 = Viajerofrecuente(3,13448845,"Jorge","sanchez",1200)
                    vi3 = vi3 == 1200
                    print(vi3) 
                   else:
                       if opcion == "f":
                        break
              