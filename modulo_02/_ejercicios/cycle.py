__author__ = 'Manuel C. D.'


import unittest
from itertools import cycle


# class MyTestCase(unittest.TestCase):
#
#     def test_ciclo(self):
#         resultado = cycle([1, 2, 3, 4])


print("Creo mi ciclo:")
miciclo = cycle("ABCDEFG")
print("--------------")

for _ in range(5):
    print(miciclo.__next__())

print("--------------")














#
# mylist = range(5)
#
#
# def funcion_con_return():
#     global mylist
#     for _ in mylist:
#         print("return", _)
#         return _*_
#
#
# def funcion_con_yield():
#     global mylist
#     for _ in mylist:
#         print("yield", _)
#         yield _*_
#
#
# print("ASIGNO a")
# a = funcion_con_return()
# print("ASIGNO b")
# b = funcion_con_yield()
#
# print("MUESTRO LOS RESULTADOS")
# print("print(a) = ", a, "\nprint(b) = ", b)
# print("----------------------")
# print("print(a) = ", a, "\nprint(list(b)) = ", list(b))
#
# print(range(0, 5))
#
# print("--------------------"
#       "--------------------")
# mygenerator = funcion_con_yield()
#
# print(list(mygenerator)[2])
#
#
# for _ in mygenerator:
#     print("  I get:", _)
#
# print("adios", mygenerator)
