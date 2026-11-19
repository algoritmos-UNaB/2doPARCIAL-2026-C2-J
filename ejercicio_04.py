from ejercicio_01 import Cancion
from ejercicio_02 import CancionNoEncontradaError


class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self._tamanio = 0

    def esta_vacia(self) -> bool:
        return self.primero is None

    def tamanio(self) -> int:
        return self._tamanio

    def insertar_al_inicio(self, dato) -> None:
        nuevo = Nodo(dato, siguiente=self.primero)
        self.primero = nuevo
        self._tamanio += 1

    def insertar_al_final(self, dato) -> None:
        nuevo = Nodo(dato, siguiente=None)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def quitar_primero(self):
        if self.primero is None:
            return None
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        self._tamanio -= 1
        return dato

    def __iter__(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Playlist:
    def __init__(self):
        self._canciones = ListaEnlazada()

    def agregar(self, cancion: Cancion) -> None:
        self._canciones.insertar_al_final(cancion)

    def quitar(self, id: int) -> Cancion:
        anterior = None
        actual = self._canciones.primero

        while actual is not None:
            if actual.dato.id == id:
                if anterior is None:
                    self._canciones.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._canciones._tamanio -= 1
                return actual.dato
            anterior = actual
            actual = actual.siguiente

        raise CancionNoEncontradaError(f"No se encontró la canción con id {id} en la playlist.")

    def listar(self) -> list[str]:
        return [str(cancion) for cancion in self._canciones]

    def duracion_total(self) -> int:
        total = 0
        for cancion in self._canciones:
            total += cancion.duracion_seg
        return total


# Teoría:
# Se recorren n nodos para avanzar desde el primer
# nodo hasta el último nodo, donde se enlaza el nuevo nodo al final.