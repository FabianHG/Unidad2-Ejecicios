"""
Autor: Fabian Hernandez Guerrero
Email: fabian.vaio@gmail.com
Fecha: 20 Febrero 2020
"""

class Login:
    def ingresar(self):
        print("                  INICIO DE SESION     ")
        print("")
        print("Para poder ingresar teclea tu usuario y contraseña")
        print("")
        user = str(input("Usuario: "))
        cont = str(input("Contraseña: "))

        if user != "utng" and cont != "mexico":
            print("")
            print("Usuario y contraseña incorrectos")
        else:
            if user == "utng":
                if cont == "mexico":
                    print("")
                    print("                  BIENVENIDO")
                else:
                    print("Contraseña incorrecta")
            else:
                print("Usuario incorrecto")
            
Login().ingresar()
        
