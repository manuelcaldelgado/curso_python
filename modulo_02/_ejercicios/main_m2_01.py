__author__ = 'Manuel C. D.'


'''
MÓDULO 2 - ejercicio_01

Se desea diseñar un fragmento de código que permita calcular números aleatorios entre un rango de dos números,
de manera que dichos números aleatorios nunca se repitan.
Por ejemplo, dado el rango [1, 6), los tres primeros números podrían ser 4, 2 y 3.
Los sucesivos números tendrían que ser distintos a todos los anteriores.

¿Cómo podría probar el diseño anterior? ¿De qué manera afectaría trabajar con resultados que se generan automáticamente?
Escriba una posible implementación y al menos un caso de prueba.

'''





import random
import unittest


#   C L A S E    L O T E R I A

class Loteria(object):

    def __init__(self, ficha_min=1, ficha_max=6):
        self._fichas = list(range(ficha_min, ficha_max+1))
        self._resultado = []
        # assert not ficha_min >= ficha_max, "La ficha pequeña es mayor que la grande"

    #   D U D A
    #
    #   Tal y como creo los objetos de la clase Loteria, es posible introducir
    #   ficha_min > ficha_max
    #   porque list(range(5, 2)) NO DA ERROR y me genera una lista vacía
    #   PERO range(5, 2) SÍ DA ERROR
    #
    #   ¿Debería controlar esto en la creación del objeto y meter un assert o algo?
    #   ¿O debo controlarlo con el test de errores?
    #

    def saca_ficha(self):
        metoca_indice = random.choice(range(len(self._fichas)))
        sacodelsaco = self._fichas.pop(metoca_indice)
        self._resultado.append(sacodelsaco)

    def resultados(self):
        for _ in range(len(self._fichas)):
            self.saca_ficha()
        return self._resultado


#   P R U E B A S      P A R A      L A      C L A S E      L O T E R I A


class MisPruebasLoteria(unittest.TestCase):

    def setUp(self):
        self.loteria_sinparam = Loteria()

    def test_inicializacion_sin_parametros(self):
        self.assertEqual(self.loteria_sinparam._fichas, [1, 2, 3, 4, 5, 6])

    def test_inicializacion_con_parametros(self):
        self.assertEqual(Loteria(3, 7)._fichas, [3, 4, 5, 6, 7])

    def test_inicializacion_minimo_negativo(self):      # Este test está condicionado por cómo creo Loteria(). Ver nota
        self.assertEqual(Loteria(-2, 1)._fichas, [-2, -1, 0, 1])

    def test_inicializacion_maximo_minimo(self):        # Este test está condicionado por cómo creo Loteria(). Ver nota
        self.assertEqual(Loteria(6, 2)._fichas, [])

    def test_sacaficha(self):
        numeros = range(len(self.loteria_sinparam._resultado))
        for numero in numeros:
            self.loteria_sinparam.saca_ficha()
            for _ in self.loteria_sinparam._resultado:
                self.assertNotIn(_, self.loteria_sinparam._fichas)

    def test_resultado_final(self):
        bolsa_llena = sorted(self.loteria_sinparam._fichas)
        resultado_final = sorted(self.loteria_sinparam.resultados())
        self.assertEqual(bolsa_llena, resultado_final)





#   ################################################################################
#
#                                    M A I N
#
#   ################################################################################

if __name__ == "__main__":

    unittest.main()

    # magic_dice = Loteria(5, -2)
    # print("Tenemos:", magic_dice._fichas)
    # print("-------------- O P E R A M O S -----------------\n")
    #
    # print("Resultados:", magic_dice.resultados())
    # print("Nos queda en el saco:", magic_dice._fichas)