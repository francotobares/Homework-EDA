import unittest
from Class import numericSecuence_class


class TestLista_Class(unittest.TestCase):


    def setUp(self):
        self.list1 = numericSecuence_class.Lista([0,1,2,3])
        self.list2 = numericSecuence_class.Lista([3,2,1])
        self.list3 = numericSecuence_class.Lista()
        self.list4 = numericSecuence_class.Lista([5, 6, 7, 8])


    def test_validate(self):

        self.assertTrue(self.list1.validate())
        self.assertFalse(self.list2.validate())


    def test_setContent(self):
        self.list3.setContent()
        self.list1.setContent([2, 3, 4, 5])
        self.assertIsNotNone(self.list3.content)
        self.assertEqual(4, len(self.list3.content))
        self.assertEqual([2,3,4,5],self.list1.content)


    def test_getContent(self):
        self.assertEqual([0,1,2,3], self.list1.getContent())

    def test_random(self):
        self.assertEqual(4, len(self.list3.random(4,9)))


    def test_comparacion(self):
        self.list1.comparacion(self.list4.content)
        self.assertEquals(4,self.list1.resultado.getIncorrecto())
        self.assertEquals(0,self.list1.resultado.getCorrectos())

    def test_listasPosicionesCondicionesAleatoriasSobreLista(self):
        self.list1.comparacion(self.list4.content)
        self.assertEquals(4, len(self.list1.listasPosicionesCondicionesAleatoriasSobreLista()[1]))
        self.assertEquals(0, len(self.list1.listasPosicionesCondicionesAleatoriasSobreLista()[0]))
        self.assertEquals(0, len(self.list1.listasPosicionesCondicionesAleatoriasSobreLista()[2]))

    def test_listaEnBaseACondicionales(self):
        self.list1.listaEnBaseACondicionales(self.list3.content)
        self.assertEquals(4, len(self.list1.content))