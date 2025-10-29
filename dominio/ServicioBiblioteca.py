from dominio.Libro import Libro
from dominio.Usuario import Usuario
from dominio.Prestamo import Prestamo
from dominio.Multa import Multa
from datetime import date, timedelta

class ServicioBiblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []
        self.multas = []

    def agregar_nuevo_libro(self, libro:Libro):
        self.libros.append(libro)
        print(f" Libro agregado: {libro.titulo} de {libro.autor}")

    def buscar_libros_por_titulo(self, titulo:str):
        return [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]

    def buscar_libros_por_autor(self, autor):
        return [libro for libro in self.libros if autor.lower() in libro.autor.lower()]

    def registrar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)
        print(f" Usuario registrado: {usuario.id} {usuario.nombre}")

    def registrar_prestamo(self, usuario: Usuario, libro: Libro):
        if libro.stock > 0:
            libro.stock -= 1
            libro.cambiar_estado(libro.stock > 0)

            # Fecha de devolución esperada: 20 días después del préstamo
            fecha_devolucion_esperada = date.today() + timedelta(days=20)
            nuevo_prestamo = Prestamo(usuario, libro, fecha_devolucion_esperada)
            self.prestamos.append(nuevo_prestamo)

            print(f" {usuario.nombre} ha pedido prestado el libro '{libro.titulo}'.")
            return True
        else:
            print(f" El libro '{libro.titulo}' no está disponible.")
            return False

    def registrar_devolucion(self, usuario: Usuario, libro: Libro, prestamo: Prestamo):
        for p in self.prestamos:
            if p.usuario == usuario and p.libro == libro and p.fecha_devolucion_real is None:
                prestamo.registrar_devolucion()
                libro.stock += 1
                libro.cambiar_estado(True)
                print(f" {usuario.nombre} devolvió '{libro.titulo}'.")
                return True

        print(f" No se encontró un préstamo activo del libro '{libro.titulo}' para {usuario.nombre}.")
        return False

    def ver_libros_disponibles(self):
        disponibles = []
        for libro in self.libros:
            estado = "Disponible " if libro.estado_disponible else "Prestado"
            print(f"{libro.titulo} - {libro.autor} : {estado}")
            if libro.estado_disponible:
                disponibles.append(libro)
        return disponibles

    def notificar_disponibilidad(self, libro: Libro):
        if libro.estado_disponible:
            print(f" El libro '{libro.titulo}' ahora está disponible nuevamente.")
        else:
            print(f" El libro '{libro.titulo}' sigue sin disponibilidad.")

    def generar_reporte(self):
        print("\n Reporte de préstamos:")
        for prestamo in self.prestamos:
            print(f"   - {prestamo}")
        print("")

    def cerrar_sesion(self) -> bool:
        print("Sesión finalizada correctamente.")
        return True
