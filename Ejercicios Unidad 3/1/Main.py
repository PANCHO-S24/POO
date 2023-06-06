from maneFacultad import ManejadorFacultad
from menu import metodo1,metodo2

if __name__ == '__main__':
   facultades = ManejadorFacultad()
   facultades.cargar_Facultad()
   while True:
      print("\nMenú de opciones:")
      print("1- Mostrar facultad y nombre de carreras que se dictan")
      print("2- Buscar carrera")
      print("3- salir")
      opcion = input("\nIngrese una opción: ")
 
      if opcion == "1":
        codigo = int(input(" ingrese el codigo de la facultad "))
        metodo1(facultades,codigo)

      else:
         if opcion == "2":
            nomb_carrera =input(" ingrese el nombre de la carrera ")
            metodo2(facultades,nomb_carrera)