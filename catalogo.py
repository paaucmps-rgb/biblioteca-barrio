# catalogo.py

class Ejemplar:
    def __init__(self, id_ejemplar, titulo, autor):
        self.id = id_ejemplar
        self.titulo = titulo
        self.autor = autor
        self.estado = "disponible"  # disponible, prestado, reservado

class Catalogo:
    def __init__(self):
        self._ejemplares = {}  # Diccionario ID -> Ejemplar

    def agregar_ejemplar(self, id_ejemplar, titulo, autor):
        self._ejemplares[id_ejemplar] = Ejemplar(id_ejemplar, titulo, autor)

    def buscar(self, titulo):
        """Busca ejemplares cuyo título coincida parcialmente."""
        return [e for e in self._ejemplares.values() if titulo.lower() in e.titulo.lower()]

    def obtener(self, id_ejemplar):
        """Devuelve un ejemplar por su ID."""
        return self._ejemplares.get(id_ejemplar)

    def marcar_prestado(self, id_ejemplar):
        """Cambia el estado del ejemplar a prestado."""
        if id_ejemplar in self._ejemplares:
            self._ejemplares[id_ejemplar].estado = "prestado"
            return True
        return False

    def marcar_reservado(self, id_ejemplar):
        """Cambia el estado del ejemplar a reservado si ya está prestado."""
        ejemplar = self.obtener(id_ejemplar)
        if ejemplar and ejemplar.estado == "prestado":
            ejemplar.estado = "reservado"
            return True
        return False