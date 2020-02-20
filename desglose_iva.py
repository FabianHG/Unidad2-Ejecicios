"""
Autor: Fabian Hernandez Guerrero
Email: fabian.vaio@gmail.com
Fecha: 20 Febrero 2020
"""

class IVA:
    def desglose(self):
        print("Muestra el desglose del IVA para saber cuanto se paga")
        print("")
        precio = int(input("¿Cúal el precio del producto? $"))
        iva = precio*.16
        siniva = precio - iva
        print("")
        print("El IVA del producto es $", iva)
        print("")
        print("Y el costo del producto sin IVA es $", siniva)
IVA().desglose()
