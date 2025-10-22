# tests/test_main_unittest.py
import unittest
from unittest.mock import patch
import io
from UI import main

class TestMain(unittest.TestCase):
    def setUp(self):
        main.libros.clear()
        main.usuarios.clear()
        main.prestamos.clear()

    @patch('builtins.input', side_effect=["Marta", "marta@mail.com"])
    def test_registrar_usuario(self, mock_input):
        main.registrar_usuario()
        self.assertEqual(len(main.usuarios), 1)
        self.assertEqual(main.usuarios[0].nombre_usuario, "Marta")

    @patch('builtins.input', side_effect=["Pedro", "", "Pedro"])
    def test_convertir_en_socio(self, mock_input):
        # first two inputs used to register user (name,email), third to convert
        main.registrar_usuario()
        main.convertir_en_socio()
        self.assertTrue(main.usuarios[0].es_socio)

    def test_devolver_libro_con_multa(self):
        # preparar usuario y libro y préstamo
        u = main.Usuario("Laura")
        u.es_socio = True
        main.usuarios.append(u)
        l = main.LibroSujeto("LibroMora")
        main.libros.append(l)
        main.prestamos["Laura"] = {"libro": l}
        # simular input: nombre socio, dias atraso 3
        with patch('builtins.input', side_effect=["Laura", "3"]):
            buf = io.StringIO()
            with patch('sys.stdout', new=buf):
                main.devolver_libro()
            output = buf.getvalue()
            self.assertIn("Multa", output)

if __name__ == '__main__':
    unittest.main()
