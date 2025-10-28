import unittest
from dominio.Libro import Libro

class TestLibro(unittest.TestCase):
    def test_cambiar_estado(self):
        libro = Libro("Carrie", "Stephen King", "Terror")
        self.assertTrue(libro.estado_disponible)  # inicial es True
        libro.cambiar_estado()
        self.assertFalse(libro.estado_disponible)
        libro.cambiar_estado()
        self.assertTrue(libro.estado_disponible)

if __name__ == "__main__":
    unittest.main()

