from dominio.Prestamo import Prestamo

class Multa:
    def __init__(self, dias_atraso: int, monto_por_dia: int = 500):
        self.dias_atraso = dias_atraso
        self.monto = dias_atraso * monto_por_dia
        self.pagada = False

    def calcular_multa(self, prestamo: Prestamo) -> float:
        dias_atraso = prestamo.verificar_atraso()
        self.monto = dias_atraso * 500
        return self.monto

    def pagar_multa(self, monto: float) -> bool:
        if monto >= self.monto:
            self.pagada = True
            print(f" Multa de ${self.monto} pagada correctamente.")
            return True
        else:
            print(f" Monto insuficiente. Falta ${self.monto - monto}.")
            return False

    def __str__(self):
        estado = "Pagada" if self.pagada else "Pendiente"
        return f"Multa de ${self.monto} por {self.dias_atraso} días de atraso ({estado})"
