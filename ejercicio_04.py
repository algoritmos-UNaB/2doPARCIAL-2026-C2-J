"""Ejercicio 4 - Playlist sobre lista enlazada."""
from ejercicio_02 import CancionNoEncontradaError

class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self._primero = None  # unica referencia guardada

    def esta_vacia(self) -> bool:
        return self._primero is None

    def tamanio(self) -> int:
        n = 0
        actual = self._primero
        while actual is not None:
            n += 1
            actual = actual.siguiente
        return n

    def insertar_al_inicio(self, dato):
        self._primero = Nodo(dato, self._primero)

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self._primero is None:
            self._primero = nuevo
            return
        actual = self._primero
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def quitar_primero(self):
        if self._primero is None:
            raise IndexError("La lista esta vacia")
        dato = self._primero.dato
        self._primero = self._primero.siguiente
        return dato

    def __iter__(self):
        actual = self._primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Playlist:
    def __init__(self):
        self._lista = ListaEnlazada()

    def agregar(self, cancion):
        self._lista.insertar_al_final(cancion)

    def quitar(self, id):
        nueva = ListaEnlazada()
        encontrada = False
        while not self._lista.esta_vacia():
            cancion = self._lista.quitar_primero()
            if cancion.id == id and not encontrada:
                encontrada = True
            else:
                nueva.insertar_al_final(cancion)
        self._lista = nueva
        if not encontrada:
            raise CancionNoEncontradaError(
                f"No existe una cancion con id {id} en la playlist")

    def listar(self):
        return [str(c) for c in self._lista]

    def duracion_total(self):
        total = 0
        for c in self._lista:
            total += c.duracion_seg
        return total


# TEORIA
# Como la lista solo guarda la referencia al primer nodo, para insertar al
# final hay que recorrer los n nodos existentes hasta llegar al ultimo
# (n recorridos; la operacion es O(n)). Con la lista vacia no se recorre ninguno.