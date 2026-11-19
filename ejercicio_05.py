# ejercicio_05.py
from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    """Se lanza al desapilar o ver el tope de una pila vacía."""
    pass


class Pila:
    def __init__(self):
        self._items = ListaEnlazada()

    def apilar(self, dato):
        self._items.insertar_al_inicio(dato)      # el tope es el primer nodo

    def desapilar(self):
        if self._items.esta_vacia():
            raise PilaVaciaError("No se puede desapilar: la pila está vacía.")
        return self._items.quitar_primero()

    def ver_tope(self):
        if self._items.esta_vacia():
            raise PilaVaciaError("No hay tope: la pila está vacía.")
        return next(iter(self._items))            # primer elemento, sin sacarlo

    def esta_vacia(self):
        return self._items.esta_vacia()


class HistorialReproduccion:
    def __init__(self):
        self._pila = Pila()

    def registrar(self, cancion):
        self._pila.apilar(cancion)

    def anterior(self):
        return self._pila.desapilar()

    def ultima(self):
        return self._pila.ver_tope()

"""El primer anterior() devuelve De Música Ligera, porque fue la última canción registrada y una pila es LIFO 
(last in, first out): el último en entrar es el primero en salir. Los siguientes anterior() devolverían Alfonsina 
y el mar y después Jijiji."""

