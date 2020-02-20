"""
Autor: Fabian Hernandez Guerrero
Email: fabian.vaio@gmail.com
Fecha: 20 Febrero 2020
"""

class Circulo:
    def areaCirculo(self):
        print("Este programa te proporciona el área de un circulo")
        print("")
        r = int(input("Ingresa el radio del circulo en cm: "))
        resultado = 3.1416*r
        print("")
        print("El área es: ", resultado, "cm^2") 

Circulo().areaCirculo()
