"""
Autor: Fabian Hernandez Guerrero
Email: fabian.vaio@gmail.com
Fecha: 20 Febrero 2020
"""
from math import factorial

class NFactorial:
    def factorial(self):
        print("Muestra el factorial de 5 números ingresados")
        print("")
        print("Ingresa los valores solicitados")
        n1 = int(input("N1: "))
        fac1 = factorial(n1)
        print("Su factorial es ", fac1)
        print("")
        n2 = int(input("N2: "))
        fac2 = factorial(n2)
        print("Su factorial es ", fac2)
        print("")
        n3 = int(input("N3: "))
        fac3 = factorial(n3)
        print("Su factorial es ", fac3)
        print("")
        n4 = int(input("N4: "))
        fac4 = factorial(n4)
        print("Su factorial es ", fac4)
        print("")
        n5 = int(input("N5: "))
        fac5 = factorial(n5)
        print("Su factorial es ", fac5)
        print("")
        print("Los factoriales obtenidos fueron los siguientes: ", fac1,", ", fac2,", ", fac3,", ", fac4,", ", fac5)
        
NFactorial().factorial()
