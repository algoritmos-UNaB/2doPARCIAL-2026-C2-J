"""Ejercicio 2 - Biblioteca."""

class CancionNoEncontradaError(Exception):
    """La cancion pedida no existe en la coleccion consultada."""


class Biblioteca:
    def __init__(self):
        self._canciones = []

    def agregar(self, cancion):
        self._canciones.append(cancion)

    def cantidad(self):
        return len(self._canciones)

    def obtener(self, id):
        for cancion in self._canciones:
            if cancion.id == id:
                return cancion
        raise CancionNoEncontradaError(
            f"No existe una cancion con id {id} en la biblioteca")

    def listar(self):
        return [str(cancion) for cancion in self._canciones]

    def __iter__(self):
        return iter(self._canciones)

# TEORIA
# La biblioteca guarda el catalogo completo: todas las canciones existentes, una sola vez cada una.
# Una playlist guarda solo una seleccion ordenada de canciones (las toma del catalogo), que puede variar o repetirse segun el usuario.
