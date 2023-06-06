from archivos import ManejadorCorreo
from clase import Email
import csv
if __name__ == "__main__":
    print("Ingrese datos")
    id = input(" ingrese id cuenta ")
    dominio = input(" ingrese dominio ")
    tipodom = input(" ingrese el tipo de dominio ")
    contrasena = input(" ingrese la contraseña ")
    unemail = Email(id, dominio, tipodom, contrasena)
    unemail.retornaEmail()
    unemail.getdominio()
    direccion = input(" ingrese direccion correo ")
    mail = Email(0,0,0,0)
    mail.crearcuenta(direccion)
    #mail.retornaEmail()
    mail.imprimeMje()
    unemail.modificarContrasena()
    lista=ManejadorCorreo()
    