"""Ejercicio 4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par
o impar.
"""

numero = int(input("ingrese un numero: "))

if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")