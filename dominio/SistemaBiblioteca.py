from dominio.Libro import Libro
from dominio.Usuario import Usuario
from dominio.Prestamo import Prestamo
from dominio.Multa import Multa
from dominio.Categoria import Categoria


class SistemaBiblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []
        self.multas = []

    def agregar_nuevo_libro(self, libro:Libro):
        self.libros.append(libro)

    def buscar_libros_por_titulo(self, titulo:str):
        return [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]

    def registrar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)
        print(f" Usuario registrado: {usuario.id} {usuario.nombre}")

    def registrar_prestamo(self, usuario: Usuario, libro: Libro):
        if usuario.pide_prestado_libro(libro):
            nuevo_prestamo = usuario.ver_historial_prestamos[-1]
            self.prestamos.append(nuevo_prestamo)
            print(f" Préstamo registrado: '{libro.titulo}' a {usuario.nombre}")
        else:
            print(" No se pudo registrar el préstamo.")

    def registrar_devolucion(self, usuario: Usuario, libro: Libro):
        usuario.pide_devolver_libro(libro)
        for prestamo in usuario.ver_historial_prestamos():
            if prestamo.libro == libro:
                dias_atraso = prestamo.verificar_atraso()
                if dias_atraso > 0:
                    multa = Multa(dias_atraso)
                    self.multas.append(multa)
                    print(f" Multa registrada: {multa}")

    def ver_libros_disponibles(self):
        disponibles = []
        for libro in self.libros:
            estado = "Disponible " if libro.estado_disponible else "Prestado"
            print(f"{libro.titulo} - {libro.autor} : {estado}")
            if libro.estado_disponible:
                disponibles.append(libro)
        return disponibles

    def notificar_disponibilidad(self, libro: Libro):
        if libro.estado_disponible and libro.stock > 0:
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
