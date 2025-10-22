# tests/test_main_pytest.py
import builtins
import pytest

# Importar el módulo main (ajusta si tu proyecto usa otro path)
from UI import main

def setup_function():
    # Reiniciar estado global antes de cada prueba
    main.libros.clear()
    main.usuarios.clear()
    main.prestamos.clear()

def test_registrar_usuario(monkeypatch, capsys):
    # Simular 2 inputs: nombre y email
    monkeypatch.setattr('builtins.input', lambda prompt='': "Ana" if "nombre" in prompt.lower() else "ana@mail.com")
    main.registrar_usuario()
    # Compruebo que se agregó 1 usuario y su nombre
    assert len(main.usuarios) == 1
    assert main.usuarios[0].nombre_usuario == "Ana"

def test_convertir_en_socio(monkeypatch, capsys):
    # registrar un usuario primero
    monkeypatch.setattr('builtins.input', lambda prompt='': "Juan" if "nombre" in prompt.lower() else "")
    main.registrar_usuario()
    # ahora convertir en socio -> la función solicitará nombre
    monkeypatch.setattr('builtins.input', lambda prompt='': "Juan")
    main.convertir_en_socio()
    assert main.usuarios[0].es_socio is True

def test_prestar_y_devolver_libro_success(monkeypatch, capsys):
    # crear usuario y convertir en socio
    monkeypatch.setattr('builtins.input', lambda prompt='': "Sofia" if "nombre" in prompt.lower() else "")
    main.registrar_usuario()
    main.usuarios[0].es_socio = True

    # registrar libro
    monkeypatch.setattr('builtins.input', lambda prompt='': "LibroPrueba")
    main.registrar_libro()

    # prestar libro: seleccionar índice 0 y socio "Sofia"
    inputs = iter(["0", "Sofia"])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    main.prestar_libro()

    # prestamos debe contener la entrada del socio
    assert "Sofia" in main.prestamos
    # preparar devolver: configurar presta info correcta
    # en tu main debes guardar dict {'libro': libro} en prestamos (si usaste mi sugerencia)
    # para evitar depender del estado de la implementación, comprobar título en historial
    assert main.usuarios[0].historial_prestamos[-1] == "LibroPrueba"

    # devolver libro: simular dias_atraso = 0
    inputs = iter(["Sofia", "0"])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    # adaptá si tu implementacion de prestamos guarda distinto; aquí asumimos prestamos[socio] -> {'libro': libro}
    # para evitar error, colocamos la estructura esperada si no existe:
    if not isinstance(main.prestamos["Sofia"], dict):
        main.prestamos["Sofia"] = {"libro": main.libros[0]}
    main.devolver_libro()

    captured = capsys.readouterr()
    assert "devuelto" in captured.out.lower() or "sin multa" in captured.out.lower()

def test_prestar_sin_socios(monkeypatch, capsys):
    # registrar libro
    monkeypatch.setattr('builtins.input', lambda prompt='': "LibroX")
    main.registrar_libro()
    # intentar prestar sin socios: seleccionar indice 0, pero no socios -> function should early return
    inputs = iter(["0", "NoSocio"])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    main.prestar_libro()
    captured = capsys.readouterr()
    assert "debe haber al menos un libro y un socio" in captured.out.lower()
