import unittest
from dominio.Libro import Libro
from dominio.Usuario import Usuario
from dominio.Prestamo import Prestamo
from dominio.Multa import Multa
from dominio.ServicioBiblioteca import ServicioBiblioteca


class TestServicioBiblioteca(unittest.TestCase):
    def setUp(self):
        self.sistema = ServicioBiblioteca()
        self.usuario = Usuario("Enzo", "Perez", "enzo11@email.com")
        self.usuario.registrar_socio()
        self.libro = Libro("Carrie", "Stephen King", "Terror", True, 1)
        self.sistema.agregar_nuevo_libro(self.libro)
        self.sistema.registrar_usuario(self.usuario)

    def test_agregar_nuevo_libro(self):
        nuevo_libro = Libro("IT", "Stephen King", "Terror", True, 1)
        self.sistema.agregar_nuevo_libro(nuevo_libro)
        self.assertIn(nuevo_libro, self.sistema.libros)

    def test_registrar_usuario(self):
        nuevo_usuario = Usuario("Juan", "Roman", "juan10@email.com")
        nuevo_usuario.registrar_socio()
        self.sistema.registrar_usuario(nuevo_usuario)
        self.assertIn(nuevo_usuario, self.sistema.usuarios)

    def test_busqueda_libro_existente(self):
        libros_encontrados = self.sistema.buscar_libros_por_titulo(self.libro.titulo)
        self.assertIn(self.libro, libros_encontrados)
        self.assertEqual(len(libros_encontrados), 1)

    def test_busqueda_autor_existente(self):
        libros_encontrados = self.sistema.buscar_libros_por_autor(self.libro.autor)
        self.assertIn(self.libro, libros_encontrados)
        self.assertEqual(len(libros_encontrados), 1)

    def test_busqueda_libro_inexistente(self):
        libros = self.sistema.buscar_libros_por_titulo("Libro inexistente")
        self.assertEqual(len(libros), 0)

    def test_busqueda_autor_inexistente(self):
        libros = self.sistema.buscar_libros_por_autor("Autor inexistente")
        self.assertEqual(len(libros), 0)

    def test_registrar_prestamo(self):
        self.assertTrue(self.libro.estado_disponible)
        self.sistema.registrar_prestamo(self.usuario, self.libro)
        prestamos_usuario = [p for p in self.sistema.prestamos if p.usuario == self.usuario]
        self.assertEqual(len(prestamos_usuario), 1)
        self.assertEqual(prestamos_usuario[0].libro, self.libro)
        self.assertIsNotNone(prestamos_usuario[0].fecha_devolucion_esperada)

    def test_registrar_devolucion(self):
        self.sistema.registrar_prestamo(self.usuario, self.libro)
        prestamos_antes = len(self.sistema.prestamos)
        # Obtener el préstamo activo
        prestamo_activo = [p for p in self.sistema.prestamos if p.usuario == self.usuario and p.libro == self.libro][0]
        resultado = self.sistema.registrar_devolucion(self.usuario, self.libro, prestamo_activo)
        self.assertTrue(resultado)
        self.assertEqual(prestamos_antes, len(self.sistema.prestamos))
        self.assertEqual(self.libro.stock, 1)
        self.assertTrue(self.libro.estado_disponible)

    def test_prestamo_libro_no_disponible(self):
        self.libro.stock = 0
        self.libro.estado_disponible = False
        resultado = self.sistema.registrar_prestamo(self.usuario, self.libro)
        self.assertFalse(resultado)

    def test_ver_libros_disponibles(self):
        disponibles = self.sistema.ver_libros_disponibles()
        self.assertIn(self.libro, disponibles)

    def test_notificar_disponibilidad(self):
            self.sistema.notificar_disponibilidad(self.libro)

    def test_generar_reporte(self):
        self.sistema.generar_reporte()

    def test_cerrar_sesion(self):
        resultado = self.sistema.cerrar_sesion()
        self.assertTrue(resultado)

if __name__ == "__main__":
    unittest.main()
