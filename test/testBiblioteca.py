import unittest 

from UI.main import *

class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.libro = LibroSujeto("Cien Años de Soledad")
        self.usuario1 = PerfilUsuario("Ana")
        self.usuario2 = PerfilUsuario("Luis")
        prestamos.clear()
        usuarios.clear()
        libros.clear()

    def test_agregar_observador(self):
        self.libro.agregar_observador(self.usuario1)
        self.assertIn(self.usuario1, self.libro.observadores)

    def test_eliminar_observador(self):
        self.libro.agregar_observador(self.usuario1)
        self.libro.eliminar_observador(self.usuario1)
        self.assertNotIn(self.usuario1, self.libro.observadores)

    def test_notificar_observadores(self):
        self.libro.agregar_observador(self.usuario1)
        self.libro.agregar_observador(self.usuario2)
        with self.assertLogs() as log:
            self.libro.cambiar_estado()  # Cambia el estado y notifica
            self.assertIn("Notificación para Ana", log.output[0])
            self.assertIn("Notificación para Luis", log.output[1])
    
    def test_calcular_multa_retraso(self):
        self.libro.agregar_observador(self.usuario1)
        dias_retraso = 5
        multa = self.libro.calcular_multa_retraso(dias_retraso)
        self.assertEqual(multa, dias_retraso * 0.50)


    def test_prestar_y_devolver_libro(self):
        usuarios.append(self.usuario1)
        libros.append(self.libro)
        
        # Prestar libro
        prestamos[self.usuario1.nombre_usuario] = self.libro.titulo
        self.libro.cambiar_estado()  # Cambia a prestado
        self.libro.agregar_observador(self.usuario1)
        
        self.assertFalse(self.libro.estado)  # El libro debe estar prestado
        self.assertIn(self.usuario1.nombre_usuario, prestamos)

        # Devolver libro
        self.libro.cambiar_estado()  # Cambia a disponible
        self.libro.eliminar_observador(self.usuario1)
        del prestamos[self.usuario1.nombre_usuario]
        
        self.assertTrue(self.libro.estado)  # El libro debe estar disponible
        self.assertNotIn(self.usuario1.nombre_usuario, prestamos)

if __name__ == "__main__":
    unittest.main()