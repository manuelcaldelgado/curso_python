__author__ = 'Manuel C. D.'

import random
import unittest


#   C L A S E    L O T E R I A

class Loteria(object):

    def __init__(self, ficha_min=1, ficha_max=6):
        self._fichas = list(range(ficha_min, ficha_max+1))
        self._resultado = []

    def saca_ficha(self):
        metoca_indice = random.choice(range(len(self._fichas)))
        #print(metoca_indice)

        sacodelsaco = self._fichas.pop(metoca_indice)
        self._resultado.append(sacodelsaco)

    def resultados(self):
        for _ in range(len(self._fichas)):
            self.saca_ficha()
        return self._resultado


#   P R U E B A S      P A R A      L A      C L A S E      L O T E R I A


class MisPruebasLoteria(unittest.TestCase):

    def test_inicializacion_sin_parametros(self):
        listadeprueba = Loteria()
        self.assertEqual(listadeprueba._fichas, [1, 2, 3, 4, 5, 6])

    def test_inicializacion_con_parametros(self):
        listadeprueba = Loteria(3, 7)
        self.assertEqual(listadeprueba._fichas, [3, 4, 5, 6, 7])

    def test_inicializacion_minimo_negativo(self):
        self.assertRaises(IndexError, Loteria(-2, 5))

    def test_inicializacion_maximo_minimo(self):
        self.assertRaises(SyntaxError, Loteria(6, 2))






#   ################################################################################
#
#                                    M A I N
#
#   ################################################################################

if __name__ == "__main__":

    magic_dice = Loteria()
    print("Tenemos:", magic_dice._fichas)
    print("-------------- O P E R A M O S -----------------\n")

    print("Resultados:", magic_dice.resultados())
    print("Nos queda en el saco:", magic_dice._fichas)