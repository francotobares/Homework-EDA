import unittest
from Class import numericSecuence_class

class TestResultados(unittest.TestCase):
    def setUp(self):
        self.list1 = numericSecuence_class.Lista([0,1,2,3])

    def test_getCorrectos(self):

        self.assertEquals(0,self.list1.resultado.getCorrectos())
        self.assertNotEqual(3,self.list1.resultado.getCorrectos())

    def test_setCorrectos(self):
        self.list1.resultado.setCorrectos(3)
        self.assertEquals(3,self.list1.resultado.getCorrectos())
        self.assertNotEqual(4, self.list1.resultado.getCorrectos())

    def test_increaseCorrectos(self):
        self.list1.resultado.increaseCorrectos()
        self.list1.resultado.increaseCorrectos()
        self.assertEquals(2,self.list1.resultado.getCorrectos())
        self.assertNotEqual(1, self.list1.resultado.getCorrectos())

    def test_limpiar(self):
        self.list1.resultado.setCorrectos(3)
        self.assertEquals(3,self.list1.resultado.getCorrectos())
        self.list1.resultado.limpiar()
        self.assertEquals(0,self.list1.resultado.getCorrectos())

    def test_validate(self):
        self.list1.resultado.setCorrectos(3)
        self.list1.resultado.setRegulares(1)
        self.assertTrue(self.list1.resultado.validate())
        self.list1.resultado.setIncorrectos(1)
        self.assertFalse(self.list1.resultado.validate())
