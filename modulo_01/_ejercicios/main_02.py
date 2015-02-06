__author__ = 'Manuel C. D.'

#   EJERCICIO 02
#
#   Escriba un iterador que devuelva números pares comenzando por el 2.

print("Módulo 01 - Ejercicio 02:\n"
      "            Muestra una lista de números múltiplos de 2\n")


number = int(input("¿Dónde corto?: "))
number_list = []
number_list2 = []

#   Mi primera propuesta. Además de que son más lineas, se deben hacer 2 operaciones por iteración:
#       if aux/2 == aux//2
#   Igual que en el ejercicio anterior se podría hacer una sola con:
#       if aux%2 == 0
for aux in range(2, number+1):
    if aux/2 == aux//2:
        number_list = number_list + [aux]
print("Primer código:", number_list)

#   También se puede omitir la condicional si hacemos que la lista vaya de 2 en e
for aux2 in range(2, number+1, 2):
    number_list2.append(aux2)
print("Refino:", number_list2)

#   Aquí ni siquiera guardamos la lista, sólo la imprimimos y es solo una linea:
print("Más simple 1:", [x for x in range(2, number+1) if x%2 == 0])

#   En este método nos ahorramos además la condicional:
print("Más simple 2:", [2*x for x in range(1, number//2+1)])


#   Hay 3 soluciones propuestas por el profesor:
#       1) con una CLASE generadora que nosotros creamos
#       2) con una FUNCION generadora de números pares que creamos
#       3) con el MÓDULO itertools