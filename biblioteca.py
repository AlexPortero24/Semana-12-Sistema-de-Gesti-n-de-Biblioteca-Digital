from libro import Libro        # Importa la clase Libro desde libro.py
from usuario import Usuario    # Importa la clase Usuario desde usuario.py

class Biblioteca:
    def __init__(self):
        self.libros = {}       # Diccionario que guarda los libros, clave=ISBN, valor=Libro
        self.usuarios = {}     # Diccionario que guarda usuarios, clave=ID, valor=Usuario

    # ------ Libros ------
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:       # Verifica si el libro ya no existe
            self.libros[libro.isbn] = libro    # Agrega el libro al diccionario
            print("Libro agregado correctamente.")  # Mensaje de confirmación
        else:
            print("Ya existe un libro con ese ISBN.")  # Mensaje si ya existe

    def quitar_libro(self, isbn):
        if isbn in self.libros:                 # Verifica si el ISBN existe
            del self.libros[isbn]               # Elimina el libro del diccionario
            print("Libro eliminado.")           # Mensaje de confirmación
        else:
            print("No se encontró ese libro.")  # Mensaje si no se encuentra

    # ------ Usuarios ------
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:  # Verifica si el ID no existe
            self.usuarios[usuario.id_usuario] = usuario  # Agrega el usuario
            print("Usuario registrado.")                 # Mensaje de confirmación
        else:
            print("Ese ID ya está registrado.")        # Mensaje si ya existe

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:      # Verifica si el usuario existe
            del self.usuarios[id_usuario]    # Elimina el usuario
            print("Usuario eliminado.")      # Mensaje de confirmación
        else:
            print("No se encontró ese usuario.")  # Mensaje si no existe

    # ------ Préstamos ------
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:  # Verifica usuario y libro
            usuario = self.usuarios[id_usuario]   # Obtiene el usuario
            libro = self.libros.pop(isbn)         # Quita el libro de la biblioteca
            usuario.prestados.append(libro)       # Lo añade a la lista de prestados del usuario
            print("Libro prestado.")              # Mensaje de confirmación
        else:
            print("No se puede prestar el libro.")  # Mensaje si no se puede prestar

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:           # Verifica que el usuario exista
            usuario = self.usuarios[id_usuario]   # Obtiene el usuario
            for libro in usuario.prestados:       # Recorre los libros prestados
                if libro.isbn == isbn:            # Si encuentra el libro
                    usuario.prestados.remove(libro)  # Lo elimina de la lista de prestados
                    self.libros[isbn] = libro        # Lo devuelve a la biblioteca
                    print("Libro devuelto.")         # Mensaje de confirmación
                    return
        print("No se pudo devolver el libro.")      # Mensaje si no se encuentra

    # ------ Métodos para guardar y cargar archivos .txt ------
    def guardar_datos(self, archivo="biblioteca.txt"):
        with open(archivo, "w", encoding="utf-8") as f:  # Abre archivo para escribir
            # Guardar libros
            f.write("[LIBROS]\n")                       # Sección libros
            for libro in self.libros.values():          # Recorre todos los libros
                f.write(f"{libro.isbn}|{libro.info[0]}|{libro.info[1]}|{libro.categoria}\n")  # Guarda info

            # Guardar usuarios
            f.write("[USUARIOS]\n")                     # Sección usuarios
            for usuario in self.usuarios.values():      # Recorre todos los usuarios
                f.write(f"{usuario.id_usuario}|{usuario.nombre}\n")  # Guarda info

            # Guardar préstamos
            f.write("[PRESTAMOS]\n")                    # Sección préstamos
            for usuario in self.usuarios.values():      # Recorre usuarios
                for libro in usuario.prestados:        # Recorre libros prestados
                    f.write(f"{usuario.id_usuario}|{libro.isbn}\n")  # Guarda info

    def cargar_datos(self, archivo="biblioteca.txt"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:  # Abre archivo para leer
                seccion = None
                for linea in f:                   # Recorre cada línea
                    linea = linea.strip()        # Elimina espacios al inicio y fin
                    if linea == "[LIBROS]":      # Detecta sección libros
                        seccion = "libros"
                        continue
                    elif linea == "[USUARIOS]":  # Detecta sección usuarios
                        seccion = "usuarios"
                        continue
                    elif linea == "[PRESTAMOS]":  # Detecta sección préstamos
                        seccion = "prestamos"
                        continue
                    elif not linea:              # Salta líneas vacías
                        continue

                    # Según la sección, guarda los datos
                    if seccion == "libros":
                        isbn, titulo, autor, categoria = linea.split("|")  # Separa info
                        self.agregar_libro(Libro(titulo, autor, categoria, isbn))  # Crea libro
                    elif seccion == "usuarios":
                        id_usuario, nombre = linea.split("|")                  # Separa info
                        self.registrar_usuario(Usuario(nombre, id_usuario))   # Crea usuario
                    elif seccion == "prestamos":
                        id_usuario, isbn = linea.split("|")                    # Separa info
                        if id_usuario in self.usuarios and isbn in self.libros:  # Verifica
                            self.prestar_libro(id_usuario, isbn)             # Prestamo

        except FileNotFoundError:
            print("No se encontró archivo de datos, iniciando nueva biblioteca...")  # Mensaje si no existe

    # ------ Búsquedas ------
    def buscar_titulo(self, titulo):
        return [libro for libro in self.libros.values() if libro.info[0].lower() == titulo.lower()]  # Devuelve lista de libros con título igual

    def buscar_autor(self, autor):
        return [libro for libro in self.libros.values() if libro.info[1].lower() == autor.lower()]   # Devuelve lista de libros del autor

    def buscar_categoria(self, categoria):
        return [libro for libro in self.libros.values() if libro.categoria.lower() == categoria.lower()]  # Devuelve lista de libros por categoría

    # ------ Libros prestados ------
    def listar_prestados(self, id_usuario):
        if id_usuario in self.usuarios:         # Verifica usuario
            return self.usuarios[id_usuario].prestados  # Devuelve lista de libros prestados
        return []                                # Si no existe usuario, devuelve lista vacía

