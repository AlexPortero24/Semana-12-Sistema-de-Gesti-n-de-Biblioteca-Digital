class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre          # Guarda el nombre del usuario
        self.id_usuario = id_usuario  # Guarda el ID único del usuario
        self.prestados = []           # Lista de libros que el usuario tiene prestados

    def __str__(self):
        # Devuelve una cadena para mostrar al usuario fácilmente
        return f"{self.nombre} (ID: {self.id_usuario})"

