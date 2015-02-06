__author__ = 'Manuel C. D.'


'''
MÓDULO 2 - ejercicio_04

Python incorpora un módulo, llamado itertools (https://docs.python.org/dev/library/itertools.html),
con muchas utilidades para trabajar con conjuntos de datos que son iterables.

Elija dos de las funciones de itertools y documente su uso utilizando únicamente casos de prueba.
El objetivo es conseguir que alguien que desconozca la función pueda conocer su funcionamiento y
extensiones sólo consultando las pruebas.

'''

import itertools
from itertools import repeat

import unittest


#   P R U E B A S   P A R A   L A   C L A S E   compress

class Testing_compress(unittest.TestCase):

    def setUp(self):
        self.testchain = "ABCD"
        self.testlist = [8, 7, "ABC", 5]
        self.testselectors1 = [1, 1, 1, 1]
        self.testselectors0 = [0, 0, 0, 0]

    def test_expected_results(self):
        test_result0 = list(itertools.compress(self.testchain, self.testselectors0))
        test_result1 = list(itertools.compress(self.testchain, self.testselectors1))
        self.assertEqual(test_result0, [])
        self.assertEqual(test_result1, ['A', 'B', 'C', 'D'])

        test_result_list0 = list(itertools.compress(self.testlist, self.testselectors0))
        test_result_list1 = list(itertools.compress(self.testlist, self.testselectors1))
        self.assertEqual(test_result_list0, [])
        self.assertEqual(test_result_list1, [8, 7, "ABC", 5])

    def test_longest_chain(self):
        test_result = list(itertools.compress(self.testchain, [1, 0]))
        self.assertEqual(test_result, ['A'])

    def test_longest_selector(self):
        testresult = list(itertools.compress(self.testchain, [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]))
        self.assertEqual(testresult, ['A', 'C'])

    def test_different_from_0_1(self):
        testresult = list(itertools.compress(self.testchain, [0.001, 25, 0.0, -1]))
        self.assertEqual(testresult, ['A', 'B', 'D'])

    def test_invalid_chain_or_selector(self):       # ¿Por qué había que poner un lambda para que no diese error?
        self.assertRaises(TypeError, lambda: itertools.compress(1024, [1, 0, 3, 1]))
        self.assertRaises(TypeError, lambda: itertools.compress("1024", 45))


#   P R U E B A S   P A R A   L A   C L A S E   repeat

# En esta prueba he importado el comando repeat del módulo itertools para que el código sea más legible...
# ¿Es una buena idea o es mejor no jugar con estas cosas?

class Testing_repeat(unittest.TestCase):

    def setUp(self):
        self.infinite10 = repeat(10)
        self.threetimes10 = repeat(10, 3)
        self.threetimes123 = repeat("123", 3)

    def test_expected_results(self):
        self.assertEqual(list(self.threetimes10), [10, 10, 10])
        self.assertEqual(list(self.threetimes123), ['123', '123', '123'])
        self.assertEqual(len(list(repeat(10, 3))), 3)

        prueba = repeat(10, 2)
        self.assertEqual(prueba.__next__(), 10)
        self.assertEqual(prueba.__next__(), 10)
        self.assertRaises(StopIteration, lambda: prueba.__next__())

        for _ in range(8):
            self.assertEqual(self.infinite10.__next__(), 10)

    def test_zero_index(self):
        self.assertEqual(list(repeat(10, 0)), [])
        self.assertRaises(StopIteration, lambda: repeat(10, 0).__next__())

    def test_negative_index(self):
        self.assertEqual(list(repeat(10, -5)), [])
        self.assertRaises(StopIteration, lambda: repeat(10, -5).__next__())

    def test_float_index(self):
        self.assertRaises(TypeError, lambda: repeat(10, 1.20))

# He tenido varios fallos del ordenador a la hora de probar el código porque me equivoco
# al escribir los iteradores infinitos y se me llena la RAM enseguida y pierdo el control...
# ¿Hay alguna forma de evitar esto? Como por ejemplo, limitar la RAM disponible para las ejecuciones...???




if __name__ == "__main__":

    unittest.main()