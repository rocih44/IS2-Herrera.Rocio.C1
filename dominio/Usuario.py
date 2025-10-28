from typing import List

class Usuario:
    _id_counter = 1

    def __init__(self, nombre: str, apellido: str, email: str, es_socio: bool = False):
        self.id = Usuario._id_counter
        Usuario._id_counter += 1
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.es_socio = es_socio
        self.historial_prestamos: List = []

    def registrar_socio(self) -> bool:
        self.es_socio = True
        print(f" {self.nombre} ahora es socio de la biblioteca.")
        return self.es_socio

    def pedir_prestado_libro(self, libro: str) -> bool:
        self.historial_prestamos.append(libro)
        print(f"{self.nombre} ha pedido prestado el libro: {libro}")
        return True

    def ver_historial_prestamos(self) -> List:
        return self.historial_prestamos

    def devolver_libro(self, libro: str) -> bool:
        if libro in self.historial_prestamos:
            self.historial_prestamos.remove(libro)
            print(f"{self.nombre} ha devuelto el libro: {libro}")
            return True
        else:
            print(f"Error: {self.nombre} no tiene prestado el libro: {libro}")
            return False

    def __str__(self):
        tipo = "Socio" if self.es_socio else "Usuario comun"
        return f"{self.nombre} {self.apellido} ({tipo})"

