"""Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
ingredientes para cada tipo de pizza aparecen a continuación.
● Ingredientes vegetarianos: Pimiento y tofu.
● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas
la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y
todos los ingredientes que lleva.

"""
opcion = str(input("Ingrese 'V' para vegetariana o 'N' para comun: ").upper())

if opcion == 'V':
    print("Ingredientes disponibles para pizzas vegetarianas: Pimiento y Tofu.")
    ingrediente_elegido = str(input("Elija un ingrediente (Pimiento o Tofu): ").capitalize())
    if ingrediente_elegido in ['Pimiento', 'Tofu']:
        es_vegetariana = True
    else:
        print("Ingrediente no válido.")
        es_vegetariana = False
else:
    print("Ingredientes disponibles para pizzas no vegetarianas: Peperoni, Jamón y Salmón.")
    ingrediente_elegido = str(input("Elija un ingrediente (Peperoni, Jamón o Salmón): ").capitalize())
    if ingrediente_elegido in ['Peperoni', 'Jamón', 'Salmón']:
        es_vegetariana = False
    else:
        print("Ingrediente no válido.")
        es_vegetariana = False

if es_vegetariana:
    print("La pizza elegida es vegetariana y lleva los siguientes ingredientes:")
    print("Mozzarella, Tomate y ", ingrediente_elegido)
else:
    print("La pizza elegida no es vegetariana y lleva los siguientes ingredientes:")
    print("Mozzarella, Tomate y ", ingrediente_elegido)
