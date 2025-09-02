
# Sistema de Gestión de Biblioteca Digital

## Descripción
Sistema en Python para gestionar una biblioteca digital. Permite administrar libros, usuarios y préstamos, con guardado automático en un archivo de texto (`biblioteca.txt`). Utiliza Programación Orientada a Objetos y colecciones de Python.

## Clases y Atributos

### Libro
- Atributos:
  - `info` (tupla): título y autor (inmutable)
  - `categoria`: categoría del libro
  - `isbn`: identificador único del libro
- Método:
  - `__str__()`: devuelve información legible del libro

### Usuario
- Atributos:
  - `nombre`: nombre del usuario
  - `id_usuario`: ID único del usuario
  - `prestados`: lista de libros prestados
- Método:
  - `__str__()`: devuelve información legible del usuario

### Biblioteca
- Atributos:
  - `libros` (diccionario): ISBN → Libro
  - `usuarios` (diccionario): ID → Usuario
- Métodos principales:
  - **Gestión de libros**
    - `agregar_libro(libro)`: añade un libro
    - `quitar_libro(isbn)`: elimina un libro
  - **Gestión de usuarios**
    - `registrar_usuario(usuario)`: registra un usuario
    - `eliminar_usuario(id_usuario)`: da de baja a un usuario
  - **Préstamos**
    - `prestar_libro(id_usuario, isbn)`: presta un libro a un usuario
    - `devolver_libro(id_usuario, isbn)`: devuelve un libro prestado
  - **Búsquedas**
    - `buscar_titulo(titulo)`: busca libros por título
    - `buscar_autor(autor)`: busca libros por autor
    - `buscar_categoria(categoria)`: busca libros por categoría
  - **Listar libros prestados**
    - `listar_prestados(id_usuario)`: lista libros que un usuario tiene prestados
  - **Persistencia**
    - `guardar_datos()`: guarda libros, usuarios y préstamos en `biblioteca.txt`
    - `cargar_datos()`: carga datos del archivo al iniciar

## Funcionalidades del Menú
1. Añadir libro
2. Quitar libro
3. Registrar usuario
4. Dar de baja usuario
5. Prestar libro
6. Devolver libro
7. Buscar libro por título
8. Buscar libro por autor
9. Buscar libro por categoría
10. Ver libros prestados de un usuario
11. Salir y guardar todos los datos automáticamente

## Guardado automático
- Cada acción que modifica libros, usuarios o préstamos guarda automáticamente los datos en `biblioteca.txt`.
- Al iniciar el sistema, los datos se cargan automáticamente para continuar gestionando la biblioteca.

