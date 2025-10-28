from datetime import date
from dominio.Usuario import Usuario
from dominio.Libro import Libro
from dominio.Multa import Multa

class Prestamo:
    def __init__(self, usuario: Usuario, libro: Libro, fecha_devolucion_esperada: date):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = date.today()
        self.fecha_devolucion_esperada = fecha_devolucion_esperada
        self.fecha_devolucion_real = None
        self.multa = None

    def registrar_devolucion(self):
        self.fecha_devolucion_real = date.today()

    def verificar_atraso(self) -> int:
        if self.fecha_devolucion_real is None:
            return 0
        atraso = self.fecha_devolucion_real- self.fecha_devolucion_esperada
        return max(atraso.days,0)

    def generar_multa(self):
        dias_atraso = self.verificar_atraso()
        if dias_atraso > 0:
            self.multa = Multa(dias_atraso)
            print ()
            return self.multa
        else:
            self.multa =  None

    def __str__(self):
        estado = "Activo" if self.fecha_devolucion_real is None else "Finalizado"
        return f"Prestamo de '{self.libro.titulo}' a {self.usuario.nombre} ({estado})"
