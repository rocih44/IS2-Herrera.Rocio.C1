class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, estado_disponible: bool = True, stock: int = 1):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.estado_disponible = estado_disponible
        self.stock = stock

    def cambiar_estado(self, nuevo_estado=None):
        if nuevo_estado is None:
            # Toggle automático
            self.estado_disponible = not self.estado_disponible
        else:
            # Asignación explícita
            self.estado_disponible = nuevo_estado
        return self.estado_disponible

    def __str__(self):
        estado = "Disponible" if self.estado_disponible else "Prestado"
        return f"'{self.titulo}' por {self.autor} - {estado} - Categoría: {self.categoria} (Stock: {self.stock})"


