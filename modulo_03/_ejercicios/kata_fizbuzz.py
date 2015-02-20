__author__ = 'Javier & Manuel C. D.'

"""

1, 2, fizz, 4, buzz, fizz, 7, 8, fizz,....., fizzbuzz

0 -> []
1 -> [1]
2 -> [1, 2]
3 -> [1, 2, Fizz]

Escribir prueba y ver que falla -> Escribir mínimo código y ver que TODAS las pruebas pasan -> Refactorizar
Babystep

"""


"""

EJERCICIO SOBRE LA KATA DEL HANGOUT

Solución particial de la kata fizzbuzz.
¿Cómo podemos refactorizar este código para que sea sencillo
modificar su comportamiento sin tener que modificar el código?

"""


import unittest


class Fizz_buzz(object):

    def __init__(self, limit_val=15, diccionario=None):
        if diccionario is None:
            self.diccionario = {3: "fizz", 5: "buzz"}
        else:
            self.diccionario = diccionario
        self.lista = self.fizzbuzz(limit_val)

    def _filtro(self, num):
        aux = ""
        for _ in self.diccionario:
            if num % _ == 0:
                aux += self.diccionario[_]
        return aux

    # def _filtro_si_3(self, num):      # Podemos quitar el filtro este porque lo hemos generalizado en _filtro
    #     return self._filtro(num)

    def fizzbuzz(self, limit_val):
        fizzbuzz_list = list()
        for num in range(1, limit_val + 1):
            next_elem = ""
            # next_elem += self._filtro_si_3(num)
            next_elem += self._filtro(num)
            if next_elem is "":
                next_elem = str(num)
            fizzbuzz_list.append(next_elem)
        return fizzbuzz_list


class FactoryFizzBuzz(object):      # Creo que esta Factory era alternativa a crear una función fizzbuzz en pruebas...??

    def fizzbuzz(self, limit_val):
        return Fizz_buzz(limit_val).lista


class TestFizzBuzz(unittest.TestCase):

    def fizzbuzz(self, limit_val, diccionario=None):      # Esto lo ponemos por si después cambiamos los nombres de las clases!!!
        return Fizz_buzz(limit_val, diccionario).lista

    def test_constructor_por_defecto(self):     # El constructor con parámetros ya lo probamos con los otros tests
        result = self.fizzbuzz(15)
        self.assertEqual(len(result), 15)

    def test_empty_fizzbuzz(self):
        result = self.fizzbuzz(0)
        self.assertEqual(0, len(result))

    def test_first_numer(self):
        result = self.fizzbuzz(2)
        self.assertEqual(result, ['1', '2'])

    def test_fizz(self):
        result = self.fizzbuzz(6)
        self.assertEqual('fizz', result[2])
        self.assertEqual('fizz', result[5])

    def test_buzz(self):
        result = self.fizzbuzz(5)
        self.assertEqual('buzz', result[4])

    def test_multiplo_3_y_5_a_la_vez(self):
        result = self.fizzbuzz(15)
        self.assertEqual('fizzbuzz', result[14])

    def test_diccionario_alternativo(self):     # Test para un "fizzbuzz" alternativo pasado como un diccionario
        alternativo = {4: "four?", 7: "boom", 2: "HEY!"}
        result = self.fizzbuzz(30, alternativo)
        self.assertEqual('HEY!four?boom', result[27])


if __name__ == '__main__':
    unittest.main()


dicprueba = {1: "I ", 2: "am ", 3: "your ", 4: "father "}
prueba = Fizz_buzz(12, dicprueba).lista
print(prueba)