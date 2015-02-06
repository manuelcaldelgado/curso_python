__author__ = 'Manuel C. D.'

# EJERCICIO 01
#
# Muestre por pantalla la secuencia de números indicados.
#
# Para cada múltiplo de 3, en vez de el número, se mostrará la cadena "FIZZ",
# para cada múltiplo de 5 la cadena "BUZZ" y para los múltiplos tanto de 3 como de 5 la cadena "FIZZBUZZ".
#
# Por ejemplo, los primeros 15 números ser ían:
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, FizzBuzz.

print("Módulo 01 - Ejercicio 01:\n"
      "            Muestra una lista de números sustituyendo los múltiplos de 3 y 5 por Fizz y Buzz, respectivamente\n")

mult3 = "Fizz"
mult5 = "Buzz"
number_list = []

number = int(input("Escribe un número: "))

for aux in range(1, number+1):
    multi = ""
    # Para ahorrar cálculos, en lugar de comprobar con      # if aux/3 == aux//3:
    # Hacemos       #   if aux%3 == 0:
    if aux%3 == 0:
        multi = multi + mult3
    if aux%5 == 0:
        multi = multi + mult5
    if multi == "":
        multi = aux
    number_list.append(multi)

print(number_list)