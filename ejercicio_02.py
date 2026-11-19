# ejercicio_02.py
from ejercicio_01 import Cancion


class CancionNoEncontradaError(Exception):
    """Se lanza cuando no existe una canción con el id pedido."""
    pass


class Biblioteca:
    def __init__(self):
        self._canciones = []

    def agregar(self, cancion):
        self._canciones.append(cancion)

    def cantidad(self):
        return len(self._canciones)

    def obtener(self, id):
        for c in self._canciones:
            if c.id == id:
                return c
        raise CancionNoEncontradaError(
            f"No existe una canción con id {id} en la biblioteca."
        )

    def listar(self):
        return [str(c) for c in self._canciones]

    def __iter__(self):
        return iter(self._canciones)


#La biblioteca guarda el catálogo completo de todas las canciones disponibles, cada una, una sola vez y identificada por su id.
#Una playlist guarda solo una selección de esas canciones, en un orden elegido por el usuario, y puede cambiar sin afectar al catálogo.