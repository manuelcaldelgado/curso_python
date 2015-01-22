__author__ = 'yakari'

#   EJERCICIO 02
#
#   Escriba un iterador que devuelva números pares comenzando por el 2.

print("Módulo 01 - Ejercicio 02:\n"
      "            Muestra una lista de números múltiplos de 2\n")


number = int(input("¿Dónde corto?: "))
number_list = []

for aux in range(2, number+1):
    if aux/2 == aux//2:
        number_list = number_list + [aux]

print(number_list)