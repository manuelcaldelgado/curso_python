__author__ = 'Manuel C. D.'

import unittest
from itertools import permutations


class MyTestCase(unittest.TestCase):

    def countInIterator(self, iterator):
        count = 0
        for _ in iterator:
            count += 1
        return count

    def crear_permutaciones(self, elementos, tamanyo=None):
        if tamanyo is None:
            tamanyo = len(elementos)
        return list(permutations(elementos, tamanyo))

    def test_permutaciones_correcto(self):
        #   ARRANGE
        esperado2 = [(1, 2), (2, 1)]

        esperado3 = [(1, 2, 3), (1, 3, 2),
                     (2, 1, 3), (2, 3, 1),
                     (3, 1, 2), (3, 2, 1)]

        #   ACT
        resultado = self.crear_permutaciones([1, 2])
        #   ASSERT
        self.assertEqual(len(resultado), 2)
        self.assertIn(esperado2[0], resultado)
        self.assertIn(esperado2[1], resultado)

        #   ACT
        resultado = self.crear_permutaciones([1, 2, 3])
        #   ASSERT
        self.assertEqual(len(resultado), 6)
        for _ in range(len(esperado3)):
            self.assertIn(esperado3[_], resultado)


    def test_permutaciones_con_parametro(self):
        #   ARRANGE

        #   ACT
        #   ASSERT parámetro negativo
        self.assertRaises(ValueError, lambda: self.crear_permutaciones([1, 2], -5))

        #   ACT
        resultado = self.crear_permutaciones([1, 2], 0)
        #   ASSERT parametro nulo
        self.assertEqual(len(resultado), 1)
        self.assertIn(tuple(), resultado)

        #   ACT
        resultado = self.crear_permutaciones([1, 2, 3], 2)
        #   ASSERT parámetro entre 1 y len(ELEMENTOS)
        self.assertEqual(len(resultado), 6)


    def test_lista_vacia(self):
        #   ARRANGE
        #   ACT
        resultado = self.crear_permutaciones([])
        self.assertEqual(len(resultado), 1)
        self.assertIn(tuple(), resultado)
        #   ASSERT
        # print("test_lista_vacia... OK")









if __name__ == '__main__':
    unittest.main()
