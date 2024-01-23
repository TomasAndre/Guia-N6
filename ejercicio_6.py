"""Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el
nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los
hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que
pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde."""

nombre = str(input("ingrese su nombre: "))
sexo = str(input("ingrese su sexo(h o m): ".lower()))

if len(nombre) > 0:
    primera_letra = nombre[0].lower()  

    if 'a' <= primera_letra <= 'm' and sexo == 'm':
        print("perteneces a la comision A")
        
    elif 'n' <= primera_letra <= 'z' and sexo == 'h':
        print("perteneces a la comision A")

    else:
        print("perteneces a la comision B")
