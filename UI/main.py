import sys
import os

# Asegura que Python pueda encontrar la carpeta src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.Observer import LibroSujeto, PerfilUsuario

libros = []
usuarios = []
prestamos = {}  

class Usuario(PerfilUsuario):  # tenemos que heredar de PerfilUsuario para mantener notificaciones
    def __init__(self, nombre, email=""):
        super().__init__(nombre)
        self.email = email
        self.es_socio = False
        self.historial_prestamos = []
        
    def registrar_socio(self):
        if not self.es_socio:
            self.es_socio = True
            print(f" Usuario '{self.nombre_usuario}' ahora es socio habilitado para préstamos.\n")
        else:
            print(f" Usuario '{self.nombre_usuario}' ya es socio.\n")

def registrar_usuario():
    nombre = input(" Ingrese el nombre del usuario: ")
    email = input(" Ingrese el email del usuario (opcional): ")
    usuario = Usuario(nombre, email)
    usuarios.append(usuario)
    print(f" Usuario '{nombre}' registrado correctamente.\n")

def convertir_en_socio():
    if not usuarios:
        print(" No hay usuarios registrados.\n")
        return
    nombre = input(" Ingrese el nombre del usuario a convertir en socio: ")
    usuario = next((u for u in usuarios if u.nombre_usuario == nombre), None)
    if usuario:
        usuario.registrar_socio()
    else:
        print(" Usuario no encontrado.\n")

def registrar_libro():
    titulo = input(" Ingrese el título del libro: ")
    libro = LibroSujeto(titulo)
    libros.append(libro)
    print(f" Libro '{titulo}' registrado correctamente.\n")

def mostrar_libros():
    if not libros:
        print(" No hay libros registrados.\n")
        return
    print(" Lista de libros:")
    for i, libro in enumerate(libros):
        estado = "Disponible" if libro.estado else "Prestado"
        print(f"  [{i}] {libro.titulo} - {estado}")
    print()

def mostrar_socios():
    socios = [u for u in usuarios if u.es_socio]
    if not socios:
        print(" No hay socios registrados.\n")
        return
    print(" Lista de socios:")
    for s in socios:
        print(f" - {s.nombre_usuario}")
    print()

def prestar_libro():
    if not libros or not any(u.es_socio for u in usuarios):
        print(" Debe haber al menos un libro y un socio registrado.\n")
        return

    mostrar_libros()
    indice = int(input("Seleccione el número del libro a prestar: "))
    if indice < 0 or indice >= len(libros):
        print(" Índice inválido.\n")
        return

    socio_nombre = input("Ingrese el nombre del socio que pide el libro: ")
    usuario = next((u for u in usuarios if u.nombre_usuario == socio_nombre and u.es_socio), None)
    if not usuario:
        print(" Ese usuario no está registrado como socio.\n")
        return

    libro = libros[indice]
    if not libro.estado:
        print(" El libro ya está prestado.\n")
        return

    libro.agregar_observador(usuario)
    libro.cambiar_estado()
    usuario.historial_prestamos.append(libro.titulo)
    prestamos[socio_nombre] = { "libro": libro}
    print(f" El libro '{libro.titulo}' fue prestado a {socio_nombre}.\n")
    

MULTA_DIARIA = 500

def devolver_libro():
    socio_nombre = input(" Ingrese el nombre del socio que devuelve el libro: ")
    if socio_nombre not in prestamos:
        print(" No hay préstamos registrados para ese socio.\n")
        return

    info_prestamo = prestamos[socio_nombre]
    libro = info_prestamo['libro']
    usuario = next((u for u in usuarios if u.nombre_usuario == socio_nombre), None)

    if libro and usuario:
        libro.cambiar_estado()
        libro.eliminar_observador(usuario)
        del prestamos[socio_nombre]

        # Solicitar al usuario cuantos días se retrasó la devolución
        dias_atraso = int(input("Ingrese la cantidad de días de retraso (0 si se devolvió a tiempo): "))
        if dias_atraso > 0:
            multa = dias_atraso * MULTA_DIARIA
            print(f" El libro fue devuelto con {dias_atraso} días de retraso. Multa: ${multa}")
        else:
            print(" Libro devuelto a tiempo. No hay multa.")

        print(f" El libro '{libro.titulo}' fue devuelto correctamente.\n")
    else:
        print(" Libro o usuario no encontrado.\n")


# Menú principal
def menu():
    while True:
        print("===== * MENÚ DE BIBLIOTECA * =====")
        print("1. Registrar usuario")
        print("2. Convertir usuario en socio")
        print("3. Registrar libro")
        print("4. Mostrar libros")
        print("5. Mostrar socios")
        print("6. Prestar libro")
        print("7. Devolver libro")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        print()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            convertir_en_socio()
        elif opcion == "3":
            registrar_libro()
        elif opcion == "4":
            mostrar_libros()
        elif opcion == "5":
            mostrar_socios()
        elif opcion == "6":
            prestar_libro()
        elif opcion == "7":
            devolver_libro()
        elif opcion == "0":
            print(" ¡Gracias por usar el sistema de biblioteca!")
            break
        else:
            print(" Opción inválida. Intente nuevamente.\n")


if __name__ == "__main__":
    menu()
