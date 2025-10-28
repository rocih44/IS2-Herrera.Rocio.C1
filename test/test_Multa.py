import unittest
from dominio.Multa import Multa

class TestMulta(unittest.TestCase):
    def test_calcular_multa(self):
        # Simula un préstamo con 5 días de atraso
        class Prestamo:
            def verificar_atraso(self):
                return 5

        prestamo = Prestamo()
        multa = Multa(0)  # Inicialmente sin días de atraso
        monto_calculado = multa.calcular_multa(prestamo)
        self.assertEqual(monto_calculado, 2500)  # 5 días * 500
        self.assertEqual(multa.monto, 2500)

    def test_pagar_multa(self):
        multa = Multa(5)  # 5 días de atraso, monto = 5 * 500 = 2500
        self.assertFalse(multa.pagada)
        self.assertTrue(multa.pagar_multa(2500))  # Pago completo
        self.assertTrue(multa.pagada)
    
    def test_pagar_multa_insuficiente(self):
        multa = Multa(5)  # 5 días de atraso, monto = 5 * 500 = 2500
        self.assertFalse(multa.pagada)
        self.assertFalse(multa.pagar_multa(1500))  # Pago insuficiente
        self.assertFalse(multa.pagada)

    def test_str(self):
        multa = Multa(5)  # 5 días de atraso, monto = 5 * 500 = 2500
        self.assertEqual(str(multa), "Multa de $2500 por 5 días de atraso (Pendiente)")
        multa.pagar_multa(2500)  # Pago completo
        self.assertEqual(str(multa), "Multa de $2500 por 5 días de atraso (Pagada)")

if __name__ == '__main__':
    unittest.main()