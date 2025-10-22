```mermaid
classDiagram
    class Libro {
        - titulo : String
        - autor : String
        - estadoDisponible : Boolean
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
        + pidePrestadoLibro(libro : Libro) : Boolean
        + pideDevolverLibro(libro : Libro) : Boolean
        + verHistorialPrestamos() : List~Prestamo~prestamos
    }

    class Prestamo {
        - fechaPrestamo : Date
        - fechaDevolucionEsperada : Date
        - fechaDevolucionReal : Date
        + verificarAtraso() : Integer 
    }

    class Multa {
        - monto : Double
        - diasAtraso : Integer
        - pagada : Boolean
        + calcularMulta(prestamo : Prestamo) : Double
        + pagarMulta(monto : Double) : Boolean
    }

    class SistemaBiblioteca {
        + buscarLibrosPorTitulo(titulo : String) : List~Libro~libros
        + agregarNuevoLibro(libro : Libro)
        + registrarPrestamo(usuario : Usuario, libro : Libro)
        + registrarDevolucion(prestamo : Prestamo)
        + notificarMultas(usuario : Usuario)
        + notificarDisponibilidad(libro : Libro)
        + verLibrosDisponibles(categoria : Categoria) : List~Libro~librosDisponibles
        + verHistorialPrestamos(usuario : Usuario) : List~Prestamo~prestamos
        + generarReporte() : List~Prestamo~prestamos
        + cerrarSesion() : Boolean
    }



    %% Relaciones entre clases
    SistemaBiblioteca "1" -- "0..*" Libro : gestiona varios
    SistemaBiblioteca "1" -- "0..*" Usuario : gestiona
    SistemaBiblioteca "1" -- "0..*" Multa : maneja
    SistemaBiblioteca "1" -- "0..*" Prestamo : coordina
    Libro "1" -- "1" Categoria : pertenece a
    Usuario "1" -- "0..*" Prestamo : hace
    Prestamo "1" -- "1" Libro : involucra
    Usuario "1" -- "0..*" Multa : puede tener
    