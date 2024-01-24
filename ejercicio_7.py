"""Ejercicio 7
Los tramos impositivos para la declaración de la renta en un determinado país son los
siguientes:
Renta                       Tipo impositivo
Menos de 10000€             5%
Entre 10000€ y 20000€       15%
Entre 20000€ y 35000€       20%
Entre 35000€ y 60000€       30%
Más de 60000€               45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo
impositivo que le corresponde.
"""

renta_anual = float(input("Ingrese su renta anual en euros: "))

if renta_anual < 10000:
    tipo_impositivo = 0.05
elif 10000 <= renta_anual < 20000:
    tipo_impositivo = 0.15
elif 20000 <= renta_anual < 35000:
    tipo_impositivo = 0.20
elif 35000 <= renta_anual < 60000:
    tipo_impositivo = 0.30
else:
    tipo_impositivo = 0.45

print(f"Su renta anual de {renta_anual} euros corresponde a un tipo impositivo del {tipo_impositivo * 100}%.")
