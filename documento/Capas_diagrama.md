```mermaid
%% Diagrama de arquitectura en 3 capas - Sistema de Biblioteca
graph TD

%% === Capa de Presentación ===
subgraph UI["🖥️ Capa de Presentación (Interfaz de Usuario)"]
    UI1["Formularios, Menús, Pantallas de préstamo y devolución"]
end

%% === Capa de Negocio ===
subgraph NEGOCIO["⚙️ Capa de Negocio (Lógica + Dominio)"]
    NEG1["Servicio y Entidades: Libro, Usuario, Préstamo, Multa, ServicioBiblioteca"]
    NEG2["Funciones de negocio: AgregarLibro, BuscarLibro, RegistrarUsuario, RegistrarPrestamo, RegistrarDevolucion"]
end

%% === Capa de Datos ===
subgraph DATOS["💾 Capa de Datos / Persistencia"]
    DAT1["Base de datos, Repositorios, Conexión SQL"]
end

%% === Conexiones entre capas ===
UI --> NEGOCIO
NEGOCIO --> DATOS