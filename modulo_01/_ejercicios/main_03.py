__author__ = 'yakari'

# EJERCICIO 03
#
# Escriba un fragmento de código que permita detectar si una lista es palíndroma.
# Una lista es palíndroma si el primer elemento es igual al último, el segundo igual al penúltimo, etc

print("Módulo 01 - Ejercicio 03:\n"
      "            Detecta si una lista dada es palíndroma o no.\n\n"
      "Debemos proporcionar una lista de palabras y/o números separadas por espacios.\n")


seguir = "s"

while seguir == "S" or seguir == "s":

    lista_gen = []
    lista_pal = [1, "rosa", "margarita", "rosa", 1]
    lista_nopal = [3, "verde", "AGUA", "FUEGO", "verde", 2]


    lista_gen = str((input("Dame una lista: "))).split()

    print(lista_gen)
    print(type(lista_gen))
    print(len(lista_gen))

    contador = len(lista_gen)

    si_no = "sí"

    for aux in range(1, contador//2+1):
        if lista_gen[aux-1] == "," or lista_gen[aux-1] == " " or lista_gen[aux-1] == "(" or lista_gen[aux-1] == "[":
            continue
        else:
            print("elemento  ", aux-1, ": ", lista_gen[aux-1])
            print("elemento ",  -aux, ": ", lista_gen[-aux])
            if lista_gen[aux-1] != lista_gen[-aux]:
                si_no = "no"
                print("                 ", si_no)
                break
            else:
                si_no= "sí"
                print("                 ", si_no)

    print("La lista suministrada " + si_no + " es palíndroma.\n")

    seguir = input("Si quieres volver a probar, introduce (s/S): ")
    print("------------------------------------------------\n")


