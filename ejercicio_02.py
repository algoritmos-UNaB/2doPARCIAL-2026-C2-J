from ejercicio_01 import Cancion


class CancionNoEncontradaError(Exception):
    pass


class Biblioteca:
    def __init__(self):
        self._canciones: list[Cancion] = []

    def agregar(self, cancion: Cancion) -> None:
        self._canciones.append(cancion)

    def cantidad(self) -> int:
        return len(self._canciones)

    def obtener(self, id: int) -> Cancion:
        for cancion in self._canciones:
            if cancion.id == id:
                return cancion
        raise CancionNoEncontradaError(f"No se encontró ninguna canción con id {id}.")

    def listar(self) -> list[str]:
        return [str(cancion) for cancion in self._canciones]

    def __iter__(self):
        return iter(self._canciones)


# Teoría:
# La biblioteca almacena el catálogo completo de canciones disponibles en el sistema.
# En cambio, una playlist guarda una secuencia ordenada de canciones seleccionadas para escuchar en un momento dado.