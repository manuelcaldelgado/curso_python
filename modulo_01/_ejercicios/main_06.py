__author__ = 'yakari'

# EJERCICIO 06
#
#
# Escriba un fragmento de código que simule varios lanzamientos de tres dados de 6 caras,
# por ejemplo 1.000 lanzamientos y muestre cuantas veces ha salido cada uno de los resultados posibles (desde 3 hasta 18)


print("Módulo 01 - Ejercicio 06:\n"
      "            Muestra la probabilidad de las distintas sumas de l dados de m caras en l lanzamientos.\n\n"
      ".\n")

import random

l = int(input("¿Cuántos dados quieres lanzar?: l = "))
m = int(input("¿De cuántas caras cada uno?: m = "))
n = int(input("¿Cuántos lanzamientos quieres hacer?: n ="))

suma_inferior = l
suma_superior = l*m
print("\nLos posibles valores de las sumas están entre", suma_inferior, "y", suma_superior, ".\n")

#   Creo una lista llena de ceros. Cada elemento representa el número de veces que ha salido una suma.
estadistica = []
sumas_posibles = []
for aux in range(suma_inferior, suma_superior+1):
    estadistica = estadistica + [0]
    sumas_posibles = sumas_posibles + [aux]

#   Tiramos los dados n veces
for aux_tiradas in range (1, n+1):
    suma = 0

    # Calculamos la suma de cada tirada
    for aux_lanzamiento in range(1, l+1):
        suma = suma + random.randrange(1,m+1)

    # Contabilizamos el resultado sumando 1 a la lista con las probabilidades
    print("Tirada número", aux_tiradas, "====>", suma)
    posicion = 3
    estadistica[suma-l] = estadistica[suma-l] + 1


print("\n---------------------------")
print("    RESULTADO:")
print("---------------------------")
for aux_suma in sumas_posibles:
    cuentas = estadistica[aux_suma-3]
    print(aux_suma, "==>", cuentas, "     Probabilidad(" + str(aux_suma) + ") =", cuentas/n, "%")
print("---------------------------")

mas_eventos = max(estadistica)
mas_probable = sumas_posibles[estadistica.index(mas_eventos)]
print("Valor más probable:", mas_probable, "con un", mas_eventos/n, "%")
print("---------------------------")

# Lo siguiente que quiero hacer es mostrar un gráfico con los resultados.