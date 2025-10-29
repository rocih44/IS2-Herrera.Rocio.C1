import unittest
from datetime import date, timedelta
from dominio.Prestamo import Prestamo

class TestPrestamo(unittest.TestCase):
    def setUp(self):
        class UsuarioMock:
            def __init__(self, nombre):
                self.nombre = nombre

        class LibroMock:
            def __init__(self, titulo):
                self.titulo = titulo

        self.usuario = UsuarioMock("Sol")
        self.libro = LibroMock("Matilda")
        self.fecha_devolucion_esperada = date.today() + timedelta(days=7)
        self.prestamo = Prestamo(self.usuario, self.libro, self.fecha_devolucion_esperada)

    def test_init(self):
        self.assertEqual(self.prestamo.usuario.nombre, "Sol")
        self.assertEqual(self.prestamo.libro.titulo, "Matilda")
        self.assertEqual(self.prestamo.fecha_devolucion_esperada, self.fecha_devolucion_esperada)
        self.assertIsNone(self.prestamo.fecha_devolucion_real)
        self.assertIsNone(self.prestamo.multa)

    def test_registrar_devolucion(self):
        self.prestamo.registrar_devolucion()
        self.assertEqual(self.prestamo.fecha_devolucion_real, date.today())

    def test_generar_multa_con_retraso(self):
        from dominio.Multa import Multa  # Import solo dentro del test
        self.prestamo.fecha_devolucion_real = self.fecha_devolucion_esperada + timedelta(days=2)
        multa = self.prestamo.generar_multa()
        self.assertIsInstance(multa, Multa)
        self.assertIsNotNone(self.prestamo.multa)

    def test_generar_multa_sin_retraso(self):

        self.prestamo.fecha_devolucion_real = self.fecha_devolucion_esperada
        self.prestamo.generar_multa()
        self.assertIsNone(self.prestamo.multa)

    def test_str_activo_y_finalizado(self):
        texto_activo = str(self.prestamo)
        self.assertIn("Activo", texto_activo)

        self.prestamo.registrar_devolucion()
        texto_finalizado = str(self.prestamo)
        self.assertIn("Finalizado", texto_finalizado)


if __name__ == "__main__":
    unittest.main()
