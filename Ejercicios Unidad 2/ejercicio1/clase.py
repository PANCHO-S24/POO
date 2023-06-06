
class Email:
    __idcuenta = " "
    __dominio = " "
    __tipodom = " "
    __contrasena = " "

    def __init__(self, idcuenta, dominio, tipodom, contrasena):  # )constructor recibe comoparametro
        self.__idcuenta = idcuenta                               # una referencia al objeto que invoca el                                                      
        self.__dominio = dominio                                  # el metodo self
        self.__tipodom = tipodom
        self.__contrasena = contrasena

    def retornaEmail(self):
        return print(f"{self.__idcuenta}@{self.__dominio}.{self.__tipodom}")

    def getdominio(self):
        return self.__dominio

    def crearcuenta(self, direccion):
        parte1 = direccion.split("@")
        idcuenta = parte1[0]
        parte2 = parte1[1].split(".")
        dominio = parte2[0]
        tipodom = parte2[1]
        print("id de la cuenta: ",idcuenta)
        print("dominio de la cuenta: ",dominio)
        print("tipo de dominio de la cuenta: ",tipodom)
    
    def imprimeMje (self):
        nomb= input("ingrese el nombre de una persona ")
        dire = input("ingrese su direccion de correo " )
        return print(f"estimado {nomb} te enviaremos tus mensajes a la direccion de correo {dire}")
    
    def modificarContrasena(self):
        contra_actual = input(" ingrese la contrasenia actual ")
        if  contra_actual == self.__contrasena:
            contra_nueva = input(" ingrese la nueva contrasenia : ")
            self.__contrasena == contra_nueva
            print("contraseña actualizada")
        else: 
            print("la contraseña actual no coincide")
        