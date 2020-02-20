"""
Autor: Fabian Hernandez Guerrero
Email: fabian.vaio@gmail.com
Fecha: 20 Febrero 2020
"""

class NParImpar:
    def parImpar(self):
        print("Muestra si el número ingresado es par o impar")
        print("")
        n = int(input("Ingresa un número: "))
        if n%2 == 0:
            print("Es PAR")
        else:
            print("Es IMPAR")
NParImpar().parImpar()
