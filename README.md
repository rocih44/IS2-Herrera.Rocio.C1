# Trabajo Práctico – Unidad 3: Diseño Arquitectónico

## Introducción al Proyecto

Este documento presenta mi implementación del Trabajo Práctico de Unidad 3, enfocado en el diseño arquitectónico de un sistema de gestión para una biblioteca. El proyecto busca desarrollar un sistema simple que maneje funciones básicas como préstamos, devoluciones, multas y notificaciones, utilizando principios de ingeniería de software. 

En esta carpeta, he creado los siguientes archivos para organizar y validar el modelo:

- **README.md**: Este archivo, es la introducción y guía general del proyecto, incluyendo explicaciones propias y las consignas del trabajo.
- **Casos.md**: Contiene una tabla en formato Markdown que detalla las tres capas principales del sistema (presentación, lógica de negocio y datos), con una breve descripción de las funciones de cada una.
- **Diagramas_Clases.md**: Incluye el esquema gráfico UML generado con Mermaid, que representa las clases, atributos, métodos y relaciones del sistema (Diagrama de clases).
- **Observer.py**: Es el archivo de código en Python que valida el modelo, implementando el patrón de diseño Observer para manejar notificaciones automáticas.


## Problemática Elegida y Uso del Patón Observer

En el contexto de este sistema de gestión de biblioteca, elegí la problemática de **notificar al usuario cuando un libro que estaba prestado se devuelve y queda disponible**. Esta es una función esencial para mejorar la experiencia del usuario, ya que evita que tengan que verificar manualmente el estado de los libros de interes personal.

Motivos para seleccionar el patrón Observer:
- El patrón Observer es ideal para este escenario porque permite que un objeto (en este caso, el libro) notifique automáticamente a otros objetos (como el perfil del usuario) cuando su estado cambia. Esto promueve un código más flexible y reactivo, sin necesidad de verificaciones constantes.
- En lugar de un enfoque manual, Observer facilita la escalabilidad en un sistema simple, asegurando que las notificaciones se envíen de manera eficiente cuando el estado del libro pasa de "prestado" a "disponible".
- Elegí este patrón por su simplicidad y relevancia, ya que resuelve el problema de notificaciones en tiempo real sin complicar el código.


## Consignas Oficiales del Trabajo

### 📝 Trabajo Práctico – Unidad 3: Diseño Arquitectónico


### **Consigna:** A partir del siguiente enunciado, deberás realizar un esquema o breve explicación escrita.

### **Enunciado:** Imaginá que estás diseñando un sistema de gestión para una **biblioteca** (préstamo de libros, registro de socios, devoluciones, etc.).

#### 1. Identificá las **tres capas principales** del sistema (presentación, lógica de negocio, datos) y escribí qué tipo de funciones tendría cada una.
#### 2. Elegí **un problema sencillo** del sistema (por ejemplo: acceso centralizado a la base de datos, control de usuarios o manejo de configuración) y explicá con tus palabras qué patrón de diseño podría ayudar a resolverlo (por ejemplo: Singleton, MVC, etc.).

### **Entrega:**
- Esquema gráfico (UML).
- Validación del modelo en el lenguaje de programación que usted elija.

## **Fecha de Entrega:**   Martes 28 de Octubre 