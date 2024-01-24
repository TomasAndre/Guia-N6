"""Ejercicio 9
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El
programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si
el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y
si es mayor de 18 años, 10€.
"""
edad = int(input("Ingrese la edad del cliente: "))

if edad < 4:
    precio_entrada = 0
elif 4 <= edad <= 18:
    precio_entrada = 5
else:
    precio_entrada = 10

print(f"El precio de entrada para un cliente de {edad} años es: {precio_entrada}€.")
