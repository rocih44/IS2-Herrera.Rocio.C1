from typing import List
from dominio.Libro import Libro

class Categoria:
    def __init__(self, nombre_tipo: str):
        self.nombre_tipo = nombre_tipo

    def buscar_por_autor(self, autor: str, libros: List[Libro]) -> List[Libro]:
        """Devuelve una lista de libros filtrados por autor."""
        return [libro for libro in libros if libro.autor.lower() == autor.lower()]

    def __str__(self):
        return f"Categoría: {self.nombre_tipo}"
