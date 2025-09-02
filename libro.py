class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)   # Guarda título y autor en una tupla (no cambia)
        self.categoria = categoria   # Guarda la categoría del libro
        self.isbn = isbn             # Guarda el ISBN del libro

    def __str__(self):
        # Devuelve una cadena para mostrar el libro fácilmente
        return f"{self.info[0]} - {self.info[1]} (ISBN: {self.isbn}, {self.categoria})"
