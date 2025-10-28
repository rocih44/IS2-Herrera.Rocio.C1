import unittest
from dominio.Usuario import Usuario

class TestUsuario(unittest.TestCase):
    def test_registrar_socio(self):
        usuario = Usuario("Rocio", "Herrera", "rocio13@gmail.com")
        self.assertFalse(usuario.es_socio)
        usuario.registrar_socio()
        self.assertTrue(usuario.es_socio)

    def test_historial_prestamos(self):
        usuario = Usuario("Rocio", "Herrera", "rocio13@gmail.com")
        usuario.historial_prestamos.append("Libro1")
        self.assertIn("Libro1", usuario.historial_prestamos)

    def test_pedir_prestado_libro(self):
        usuario = Usuario("Ana", "Garcia", "ana@gmail.com")
        usuario.pedir_prestado_libro("It")
        self.assertIn("It", usuario.historial_prestamos)

    def test_devolver_libro(self):
        usuario = Usuario("Ana", "Garcia", "ana@gmail.com")
        # Primero pedimos prestado el libro
        usuario.pedir_prestado_libro("It")
        # Luego lo devolvemos
        resultado = usuario.devolver_libro("It")
        self.assertTrue(resultado)
        self.assertNotIn("It", usuario.historial_prestamos)

if __name__ == "__main__":
    unittest.main()

