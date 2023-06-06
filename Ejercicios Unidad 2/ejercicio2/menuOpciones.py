from claseviajero import Viajerofrecuente
import csv
numero = input("Ingrese el numero del viajero: ")
viajero = Viajerofrecuente(numero,23566788,"leonel","messi",4000)    

while True:
      print("\nMenú de opciones:")
      print("a- Consultar Cantidad de Millas")
      print("b- Acumular Millas")
      print("c- Canjear Millas")
      print("d- Salir")
      opcion = input("\nIngrese una opción: ")

      if opcion == "a":
        print("\n La cantidad de millas acumuladas son \n",viajero.retorna_millas())
      else:
         if opcion == "b":
           Mrecorridas =int(input("\n ingrese la cantidad de millas a acumular \n"))
           viajero.acumularMillas(Mrecorridas)    
         else:
             if opcion== "c":
                CMillas = int(input("\n ingrese la cantidad de millas que desea canjear \n"))
                viajero.canjearMillas(CMillas)
             else:
              if opcion == "d":
                break
              else:
                print("opcion no valida,vuelva a elegir otra opcion")
