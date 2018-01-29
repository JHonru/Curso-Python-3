# -*- coding: utf-8 -*-
from __future__ import unicode_literals
numeros = [1, 3, 6, 9]
while True:
    dato = int(input("Introduce un número del 0 al 9: "))
    if dato>=0 and dato<=9:
        if dato in numeros:
            print("El número está en el listado")
        else:
            print("El número no esta en el listado")
            break
    else:
        print("El número no está en el rango solicitado")