from dominio.Categoria import Categoria

class Libro:
    def __init__(self, titulo: str, autor: str, categoria : Categoria, estado_disponible: bool = True, stock: int = 1):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.estado_disponible = estado_disponible
        self.stock = stock

    def cambiar_estado(self, estado_disponible: bool) -> bool:
        """Cambia el estado del libro y devuelve el nuevo estado."""
        self.estado_disponible = estado_disponible
        return self.estado_disponible

    def __str__(self):
        estado = "Disponible" if self.estado_disponible else "Prestado"
        cate= self.categoria.nombre_tipo if self.categoria else "Sin categoría"
        return f"{self.titulo} - {self.autor} ({estado}, Stock: {self.stock}, Categoría: {cate})"
