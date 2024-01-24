"""Ejercicio 8
En una determinada empresa, sus empleados son evaluados al final de cada año. Los
puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados
pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A
continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La
cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del
nivel.
Nivel               Puntuación
Inaceptable         0.0
Aceptable           0.4
Meritorio           0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así
como la cantidad de dinero que recibirá el usuario.
"""
puntuacion = float(input("Ingrese la puntuación del empleado: "))

if puntuacion == 0.0:
    nivel_rendimiento = "Inaceptable"
    cantidad_dinero = 0
elif puntuacion == 0.4:
    nivel_rendimiento = "Aceptable"
    cantidad_dinero = 2400 * 0.4
elif puntuacion >= 0.6:
    nivel_rendimiento = "Meritorio"
    cantidad_dinero = 2400 * puntuacion
else:
    nivel_rendimiento = "Puntuación no válida"
    cantidad_dinero = 0

print(f"Nivel de rendimiento: {nivel_rendimiento}")
print(f"Cantidad de dinero: {cantidad_dinero}€")
