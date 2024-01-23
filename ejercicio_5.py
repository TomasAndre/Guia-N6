"""Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos
iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su
edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""

edad = int(input("Ingrese su edad: "))
ingresos_mensuales = int(input("Ingrese su ingreso mensual: "))

if edad > 16 and ingresos_mensuales >= 1000:
    print("tenes que tributar")
else:
    print("no tenes que tributar")