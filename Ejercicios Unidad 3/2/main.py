from ManejaHelados import manejadorHelado
from ManejaSabores import manejadorSabor
from ClaseHelado import Helado

if __name__ == "__main__":
    manejaSabor = manejadorSabor()
    manejaSabor.cargarSabores()
    manejaHelados = manejadorHelado()

    while True:
        print("Menú de opciones:")
        print("1. Registrar un helado vendido")
        print("2. Cerrar pedido")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            # Crea al objeto helado
            print("------------------------------------------------------------------------")
            gramos = int(input("Ingrese los gramos del helado: "))
            precio = int(input("Ingrese el precio del helado: "))
            sabores = input("Ingrese los sabores del helado separados por comas: ").split(",")
            print("------------------------------------------------------------------------")
            helado_obj = Helado(gramos, precio, sabores)
            # Registra el helado vendido
            manejaHelados.registrarHelado(helado_obj)
            print("Helado registrado con éxito!")
            print("Sabores elegidos: ", ", ".join(sabores))
        else:   
            if opcion == "2":
               manejaHelados.cerrarPedido()
            else:
                if opcion == "3": 
                   manejaHelados.obtenersabormaspedido()
                else:
                    if opcion ==" 4":
                       num_sabor = int(input("Ingrese el número del sabor: "))
                       manejaHelados.gramos_vendidos(num_sabor)
       
           
        