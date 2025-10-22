```mermaid
classDiagram
    class Libro {
        - titulo : String
        - autor : String
        - estadoDisponible : Boolean
        - categoria : String
        - stock : Integer
        + cambiarEstado(estadoDisponible : Boolean) : Boolean
    }

    class Categoria {
        - nombreTipo : String
        + buscarPorAutor(autor : String) : List~Libro~libros
    }

    class Usuario {
        - id : Integer
        - nombre : String
        - apellido : String
        - email : String
        - es_socio : Boolean
        + registrar_socio() : Boolean
        + pidePrestadoLibro(libro : Libro) : Boolean
        + pideDevolverLibro(libro : Libro) : Boolean
        + verHistorialPrestamos() : List~Prestamo~prestamos
    }

    class Prestamo {
        - fechaPrestamo : Date
        - fechaDevolucionReal : Date
        + registrarDevolucion() : Boolean
        + verificarAtraso() : Integer 
        + generarMulta() : Boolean
    }

    class Multa {
        - monto : Double
        - diasAtraso : Integer
        - pagada : Boolean
        + calcularMulta(prestamo : Prestamo) : Double
        + pagarMulta(monto : Double) : Boolean
    }

    class SistemaBiblioteca {
        + agregarNuevoLibro(libro : Libro)
        + buscarLibrosPorTitulo(titulo : String) : List~Libro~libros
        + registrarPrestamo(usuario : Usuario, libro : Libro)
        + registrarUsuario(usuario : Usuario)
        + registrarDevolucion(prestamo : Prestamo)
        + verLibrosDisponibles(categoria : Categoria) : List~Libro~librosDisponibles
        + notificarDisponibilidad(libro : Libro)
        + generarReporte() : List~Prestamo~prestamos
        + cerrarSesion() : Boolean
    }

    %% Relaciones entre clases
    SistemaBiblioteca "1" -- "0..*" Libro : gestiona varios
    SistemaBiblioteca "1" -- "0..*" Usuario : gestiona
    SistemaBiblioteca "1" -- "0..*" Multa : calcula
    SistemaBiblioteca "1" -- "0..*" Prestamo : coordina
    Libro "1" -- "1" Categoria : pertenece a
    Usuario "1" -- "0..*" Prestamo : hace
    Prestamo "1" -- "1" Libro : involucra
    Usuario "1" -- "0..*" Multa : puede tener