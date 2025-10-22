from dominio.Prestamo import Prestamo
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
        self.historial_prestamos: List[Prestamo] = []

    def registrar_socio(self) -> bool:
        self.es_socio = True
        print(f"✅ {self.nombre} ahora es socio de la biblioteca.")
        return self.es_socio

    def pide_prestado_libro(self, libro):
        if libro.estadoDisponible and libro.stock > 0:
            libro.stock -= 1
            libro.cambiarEstado(libro.stock > 0)
            prestamo = Prestamo(self, libro)
            self.historial_prestamos.append(prestamo)
            print(f"📚 {self.nombre} ha pedido prestado '{libro.titulo}'.")
            return True
        else:
            print(f"⚠️ El libro '{libro.titulo}' no está disponible.")
            return False

    def pide_devolver_libro(self, libro):
        for prestamo in self.historial_prestamos:
            if prestamo.libro == libro and prestamo.fechaDevolucionReal is None:
                prestamo.registrarDevolucion()
                libro.stock += 1
                libro.cambiarEstado(True)
                print(f"✅ {self.nombre} devolvió '{libro.titulo}'.")
                return True
        print(f"⚠️ No se encontró préstamo activo del libro '{libro.titulo}'.")
        return False

    def ver_historial_prestamos(self) -> List[Prestamo]:
        return self.historial_prestamos

    def __str__(self):
        tipo = "Socio" if self.es_socio else "Usuario común"
        return f"{self.nombre} {self.apellido} ({tipo})"
