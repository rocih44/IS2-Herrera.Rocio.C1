import unittest
from datetime import date, timedelta
from dominio.Prestamo import Prestamo


class TestPrestamo(unittest.TestCase):

    def setUp(self):
        # Clases simuladas (sin importar otras entidades)
        class UsuarioMock:
            def __init__(self, nombre):
                self.nombre = nombre

        class LibroMock:
            def __init__(self, titulo):
                self.titulo = titulo

        self.usuario = UsuarioMock("Ana")
        self.libro = LibroMock("It")
        self.fecha_devolucion_esperada = date.today() + timedelta(days=7)
        self.prestamo = Prestamo(self.usuario, self.libro, self.fecha_devolucion_esperada)

    # ---- TEST: __init__ ----
    def test_init(self):
        """Verifica que el préstamo se inicialice correctamente"""
        self.assertEqual(self.prestamo.usuario.nombre, "Ana")
        self.assertEqual(self.prestamo.libro.titulo, "It")
        self.assertEqual(self.prestamo.fecha_devolucion_esperada, self.fecha_devolucion_esperada)
        self.assertIsNone(self.prestamo.fecha_devolucion_real)
        self.assertIsNone(self.prestamo.multa)

    # ---- TEST: registrar_devolucion ----
    def test_registrar_devolucion(self):
        """Debe registrar la fecha de devolución correctamente"""
        self.prestamo.registrar_devolucion()
        self.assertEqual(self.prestamo.fecha_devolucion_real, date.today())

    # ---- TEST: generar_multa ----
    def test_generar_multa_con_retraso(self):
        """Debe generar una multa si hay atraso"""
        from dominio.Multa import Multa  # Import solo dentro del test
        self.prestamo.fecha_devolucion_real = self.fecha_devolucion_esperada + timedelta(days=2)
        multa = self.prestamo.generar_multa()
        self.assertIsInstance(multa, Multa)
        self.assertIsNotNone(self.prestamo.multa)

    def test_generar_multa_sin_retraso(self):
        """No debe generar multa si no hay atraso"""
        self.prestamo.fecha_devolucion_real = self.fecha_devolucion_esperada
        self.prestamo.generar_multa()
        self.assertIsNone(self.prestamo.multa)

    # ---- TEST: __str__ ----
    def test_str_activo_y_finalizado(self):
        """Debe mostrar el estado 'Activo' o 'Finalizado' correctamente"""
        texto_activo = str(self.prestamo)
        self.assertIn("Activo", texto_activo)

        self.prestamo.registrar_devolucion()
        texto_finalizado = str(self.prestamo)
        self.assertIn("Finalizado", texto_finalizado)


if __name__ == "__main__":
    unittest.main()
