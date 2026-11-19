# ejercicio_06.py
from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    """Se lanza al desencolar o ver el frente de una cola vacía."""
    pass


class Cola:
    def __init__(self):
        self._items = ListaEnlazada()

    def encolar(self, dato):
        self._items.insertar_al_final(dato)

    def desencolar(self):
        if self._items.esta_vacia():
            raise ColaVaciaError("No se puede desencolar: la cola está vacía.")
        return self._items.quitar_primero()

    def ver_frente(self):
        if self._items.esta_vacia():
            raise ColaVaciaError("No hay frente: la cola está vacía.")
        return next(iter(self._items))            # primer elemento, sin sacarlo

    def esta_vacia(self):
        return self._items.esta_vacia()


class ColaReproduccion:
    """Cola "up next"."""

    def __init__(self):
        self._cola = Cola()

    def encolar_cancion(self, cancion):
        self._cola.encolar(cancion)

    def siguiente(self):
        return self._cola.desencolar()

    def que_sigue(self):
        return self._cola.ver_frente()

"""El primer siguiente() devuelve Jijiji, porque la cola es FIFO (first in, first out): la primera canción en entrar es 
la primera en salir. La diferencia con la pila del ejercicio 5 es el orden de salida porque la pila es LIFO y habría devuelto 
primero De Música Ligera (la última registrada), mientras que la cola respeta el orden de llegada y devuelve Jijiji, Alfonsina 
y el mar y De Música Ligera, en ese orden."""

