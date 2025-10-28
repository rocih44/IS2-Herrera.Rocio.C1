# test/test_main_unittest.py
import unittest
import UI.main as main


class TestBiblioteca(unittest.TestCase):

    def setUp(self):
        # limpiar las listas antes de cada prueba
        main.libros.clear()
        main.usuarios.clear()
        main.prestamos.clear()

    def test_registrar_socio(self):
        usuario = main.Usuario("Rocio", "rocio@mail.com")
        self.assertFalse(usuario.es_socio)  # al principio no es socio
        usuario.registrar_socio()
        self.assertTrue(usuario.es_socio)   # ahora debe ser socio

    def test_registrar_usuario(self):
        # simula registrar un usuario directamente (sin input)
        usuario = main.Usuario("Lucia", "lucia@mail.com")
        main.usuarios.append(usuario)
        self.assertEqual(len(main.usuarios), 1)
        self.assertEqual(main.usuarios[0].nombre_usuario, "Lucia")

    def test_registrar_libro(self):
        # simula registrar un libro manualmente
        from src.Observer import LibroSujeto
        libro = LibroSujeto("Carrie")
        main.libros.append(libro)
        self.assertEqual(len(main.libros), 1)
        self.assertEqual(main.libros[0].titulo, "Carrie")

    def test_convertir_en_socio(self):
        usuario = main.Usuario("Carlos", "carlos@mail.com")
        main.usuarios.append(usuario)
        usuario.registrar_socio()
        self.assertTrue(usuario.es_socio)

    def test_prestar_y_devolver_libro(self):
        from src.Observer import LibroSujeto

        # Crear usuario socio
        usuario = main.Usuario("Marta")
        usuario.registrar_socio()
        main.usuarios.append(usuario)

        # Crear libro disponible
        libro = LibroSujeto("Cien años de soledad")
        main.libros.append(libro)

        # Prestar el libro
        libro.cambiar_estado()  # simula préstamo
        usuario.historial_prestamos.append(libro.titulo)
        main.prestamos[usuario.nombre_usuario] = {"libro": libro}

        self.assertFalse(libro.estado)  # ahora debe estar prestado
        self.assertIn(usuario.nombre_usuario, main.prestamos)

        # Devolver el libro
        libro.cambiar_estado()  # vuelve a estar disponible
        del main.prestamos[usuario.nombre_usuario]
        self.assertTrue(libro.estado)
        self.assertNotIn(usuario.nombre_usuario, main.prestamos)

    def test_multas_simples(self):
        # Verifica cálculo de multa sin funciones complejas
        dias_atraso = 3
        multa = dias_atraso * main.MULTA_DIARIA
        self.assertEqual(multa, 1500)


if __name__ == "__main__":
    unittest.main()



#Las funciones mostrar_libros() y mostrar_socios() son testeados con pruebas de caja negra ( Basada en la salida esperada), no me arriesgue a probar con unittest.

#Resultado, se aprobaron las siguiente funciones: registrar_socio, registrar_usuario, convertir_en_socio, registrar_libro, prestar_libro, devolver_libro. Ademas, la funcion de calculo de multas simples.