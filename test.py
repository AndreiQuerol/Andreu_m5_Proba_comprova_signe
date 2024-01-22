import unittest
from check_number import comprova_signe

class TestProva(unittest.TestCase):
    """Les funcions de esta classes son: provar el numero positiu, negatiu i 0"""
    
    def test_comprova_signe_positiu(self):
        """Prova si el numero es positiu"""
        resultat = 1
        num=comprova_signe(5)
        self.assertEqual(resultat,1)

    def test_comprova_singe_0(self):
        """Prova si el numero es 0"""
        resultat = 0
        num=comprova_signe(0)
        self.assertEqual(resultat,0)

    def test_comprova_singe_Negatiu(self):
        """Prova si el numero es negatiu"""
        resultat = -1
        num=comprova_signe(-5)
        self.assertEqual(resultat,-1)


if __name__ == '__main__':
    unittest.main()