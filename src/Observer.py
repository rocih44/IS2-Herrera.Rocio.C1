# Importamos la biblioteca para crear interfaces abstractas (opcional, pero útil)
from abc import ABC, abstractmethod

# Paso 1: Se define la interfaz para el Observador
class Observador(ABC):
    """Interfaz abstracta para los observadores. Define el método que se llamará cuando haya un cambio."""
    @abstractmethod
    def actualizar(self, mensaje: str):
        pass

# Paso 2: Se define la clase para el Sujeto (el libro)
class LibroSujeto:
    """Clase que representa el libro como el sujeto. Mantiene una lista de observadores."""
    def __init__(self, titulo: str):
        self.titulo = titulo  
        self.estado = True # Estado inicial: true (disponible), false (prestado)
        self.observadores = []  
    
    def agregar_observador(self, observador: Observador):
        self.observadores.append(observador)
    
    def eliminar_observador(self, observador: Observador):
        if observador in self.observadores:
            self.observadores.remove(observador)
            print(f"Observador eliminado: {observador.nombre_usuario}")
        else:
            print(f"El observador {observador.nombre_usuario} no estaba suscrito.")

    
    def notificar_observadores(self):
        estado_str = "disponible" if self.estado else "prestado"
        mensaje = f"El libro '{self.titulo}' ahora está '{estado_str}'."
        for observador in self.observadores:
            observador.actualizar(mensaje)  # Llama al método actualizar de cada observador
    
    def cambiar_estado(self):
        self.estado = not self.estado  # Alterna el estado del libro
        estado_str = "disponible" if self.estado else "prestado"
        print(f"Estado del libro '{self.titulo}' cambiado a '{estado_str}'.")
        self.notificar_observadores()  # Notifica después del cambio

# Paso 3: Se define una clase concreta para el Observador 
class PerfilUsuario(Observador):
    """Clase que implementa el observador para notificar al usuario."""
    def __init__(self, nombre_usuario: str):
        self.nombre_usuario = nombre_usuario  # Nombre del usuario
    
    def actualizar(self, mensaje: str):
        """Método que se ejecuta cuando hay una notificación."""
        print(f"Notificación para {self.nombre_usuario}: {mensaje}")

# Pruebas
if __name__ == "__main__":
    libro= LibroSujeto("El Principito")
    usuario1 = PerfilUsuario("Lucía")
    usuario2 = PerfilUsuario("Carlos")
    libro.agregar_observador(usuario1)
    libro.agregar_observador(usuario2)
    libro.cambiar_estado()  # prestado
    libro.cambiar_estado()  # disponible → notifica a ambos
    libro.eliminar_observador(usuario1)