
from libro import Libro              # Importa la clase Libro desde libro.py
from usuario import Usuario          # Importa la clase Usuario desde usuario.py
from biblioteca import Biblioteca    # Importa la clase Biblioteca desde biblioteca.py

def menu():
    biblioteca = Biblioteca()        # Crea un objeto Biblioteca
    biblioteca.cargar_datos()        # Carga los datos guardados desde archivo, si existen

    while True:                      # Bucle infinito para mostrar el menú hasta que el usuario salga
        print("\n--- MENÚ BIBLIOTECA ---")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro por título")
        print("8. Buscar libro por autor")
        print("9. Buscar libro por categoría")
        print("10. Ver libros prestados")
        print("11. Salir")

        opcion = input("Elige una opción: ")  # Pide al usuario elegir una opción

        if opcion == "1":  # Añadir libro
            titulo = input("Título: ")       # Pide el título
            autor = input("Autor: ")         # Pide el autor
            categoria = input("Categoría: ") # Pide la categoría
            isbn = input("ISBN: ")           # Pide el ISBN
            libro = Libro(titulo, autor, categoria, isbn)  # Crea un objeto Libro
            biblioteca.agregar_libro(libro)   # Agrega el libro a la biblioteca
            biblioteca.guardar_datos()        # Guarda automáticamente los cambios
            print(" Libro agregado y guardado.")  # Mensaje de confirmación

        elif opcion == "2":  # Quitar libro
            isbn = input("ISBN del libro a quitar: ")  # Pide ISBN del libro
            biblioteca.quitar_libro(isbn)             # Quita el libro
            biblioteca.guardar_datos()                # Guarda automáticamente
            print("Libro eliminado y guardado.")      # Mensaje de confirmación

        elif opcion == "3":  # Registrar usuario
            nombre = input("Nombre: ")           # Pide el nombre del usuario
            id_usuario = input("ID: ")           # Pide el ID del usuario
            usuario = Usuario(nombre, id_usuario)       # Crea un objeto Usuario
            biblioteca.registrar_usuario(usuario)       # Registra el usuario
            biblioteca.guardar_datos()                   # Guarda automáticamente
            print("Usuario registrado y guardado.")     # Mensaje de confirmación

        elif opcion == "4":  # Dar de baja usuario
            id_usuario = input("ID del usuario: ")     # Pide el ID del usuario
            biblioteca.eliminar_usuario(id_usuario)    # Elimina el usuario
            biblioteca.guardar_datos()                 # Guarda automáticamente
            print("Usuario eliminado y guardado.")     # Mensaje de confirmación

        elif opcion == "5":  # Prestar libro
            id_usuario = input("ID del usuario: ")     # Pide ID del usuario
            isbn = input("ISBN del libro: ")           # Pide ISBN del libro
            biblioteca.prestar_libro(id_usuario, isbn) # Presta el libro al usuario
            biblioteca.guardar_datos()                 # Guarda automáticamente

        elif opcion == "6":  # Devolver libro
            id_usuario = input("ID del usuario: ")     # Pide ID del usuario
            isbn = input("ISBN del libro: ")           # Pide ISBN del libro
            biblioteca.devolver_libro(id_usuario, isbn)  # Devuelve el libro
            biblioteca.guardar_datos()                  # Guarda automáticamente

        elif opcion == "7":  # Buscar por título
            titulo = input("Título: ")                  # Pide título a buscar
            resultados = biblioteca.buscar_titulo(titulo)  # Busca libros por título
            if resultados:
                for libro in resultados:
                    print(libro)                        # Muestra cada libro encontrado
            else:
                print("No encontrado.")                 # Mensaje si no hay resultados

        elif opcion == "8":  # Buscar por autor
            autor = input("Autor: ")                    # Pide autor a buscar
            resultados = biblioteca.buscar_autor(autor)  # Busca libros por autor
            if resultados:
                for libro in resultados:
                    print(libro)                        # Muestra cada libro encontrado
            else:
                print("No encontrado.")                 # Mensaje si no hay resultados

        elif opcion == "9":  # Buscar por categoría
            categoria = input("Categoría: ")           # Pide categoría a buscar
            resultados = biblioteca.buscar_categoria(categoria)  # Busca libros por categoría
            if resultados:
                for libro in resultados:
                    print(libro)                        # Muestra cada libro encontrado
            else:
                print("No encontrado.")                 # Mensaje si no hay resultados

        elif opcion == "10":  # Ver libros prestados
            id_usuario = input("ID del usuario: ")      # Pide ID del usuario
            prestados = biblioteca.listar_prestados(id_usuario)  # Obtiene libros prestados
            if prestados:
                for libro in prestados:
                    print(libro)                        # Muestra cada libro prestado
            else:
                print("No tiene libros prestados.")    # Mensaje si no hay préstamos

        elif opcion == "11":  # Salir
            biblioteca.guardar_datos()                 # Guarda datos antes de salir
            print("Datos guardados. Saliendo...")      # Mensaje de salida
            break                                      # Termina el bucle y cierra el menú

        else:
            print("Opción no válida.")                 # Mensaje si se ingresa algo incorrecto

if __name__ == "__main__":
    menu()  # Ejecuta la función menú si se corre este archivo directamente
