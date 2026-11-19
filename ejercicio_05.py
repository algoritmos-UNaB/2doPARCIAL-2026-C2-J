"""Ejercicio 5 - Historial de reproduccion (Pila)."""
from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    """Se intento desapilar o ver el tope de una pila vacia."""


class Pila:
    def __init__(self):
        self._lista = ListaEnlazada()

    def apilar(self, dato):
        self._lista.insertar_al_inicio(dato)

    def desapilar(self):
        if self._lista.esta_vacia():
            raise PilaVaciaError("No se puede desapilar: la pila esta vacia")
        return self._lista.quitar_primero()

    def ver_tope(self):
        if self._lista.esta_vacia():
            raise PilaVaciaError("No hay tope: la pila esta vacia")
        return next(iter(self._lista))

    def esta_vacia(self):
        return self._lista.esta_vacia()


class HistorialReproduccion:
    def __init__(self):
        self._pila = Pila()

    def registrar(self, cancion):
        self._pila.apilar(cancion)

    def anterior(self):
        return self._pila.desapilar()

    def ultima(self):
        return self._pila.ver_tope()


# TEORIA
# El primer anterior() devuelve De Musica Ligera. La pila es LIFO (ultimo en
# entrar, primero en salir): se apilo Jijiji, luego Alfonsina y el mar y por
# ultimo De Musica Ligera, que quedo en el tope y es la primera en desapilarse.