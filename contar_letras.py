"""
Autor: Fabian Hernandez Guerrero
Email: fabian.vaio@gmail.com
Fecha: 20 Febrero 2020
"""

class Letras:
    def contarLetras(self):
        print("Este programa te cuenta los caracteres de las palabra tecleadas")
        print("")
        palabra = str(input("Ingresa una palabra: "))
        contar = len(palabra)
        print("")
        print("Tu palabra tiene " + str(contar) + " letras")
        
Letras().contarLetras()
