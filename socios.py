# socios.py

class Socio:
    def __init__(self, id_socio, nombre):
        self.id = id_socio
        self.nombre = nombre
        self.sancionado = False
        self.libros_prestados = []  # Lista de IDs de ejemplares prestados

class Socios:
    def __init__(self):
        self._socios = {}

    def registrar_socio(self, id_socio, nombre):
        if id_socio not in self._socios:
            self._socios[id_socio] = Socio(id_socio, nombre)
            return True
        return False

    def obtener(self, id_socio):
        return self._socios.get(id_socio)

    def puede_pedir(self, id_socio):
        """Verifica si el socio no está sancionado y tiene menos de 2 libros."""
        socio = self.obtener(id_socio)
        if not socio or socio.sancionado:
            return False
        if len(socio.libros_prestados) >= 2:
            return False
        return True

    def agregar_prestamo_socio(self, id_socio, id_ejemplar):
        socio = self.obtener(id_socio)
        if socio and len(socio.libros_prestados) < 2:
            socio.libros_prestados.append(id_ejemplar)
            return True
        return False

    def sancionar_socio(self, id_socio, estado=True):
        socio = self.obtener(id_socio)
        if socio:
            socio.sancionado = estado
            return True
        return False
    