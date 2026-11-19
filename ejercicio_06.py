"""Ejercicio 6 - Cola de reproduccion (up next)."""
from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    """Se intento desencolar o ver el frente de una cola vacia."""


class Cola:
    def __init__(self):
        self._lista = ListaEnlazada()

    def encolar(self, dato):
        self._lista.insertar_al_final(dato)

    def desencolar(self):
        if self._lista.esta_vacia():
            raise ColaVaciaError("No se puede desencolar: la cola esta vacia")
        return self._lista.quitar_primero()

    def ver_frente(self):
        if self._lista.esta_vacia():
            raise ColaVaciaError("No hay frente: la cola esta vacia")
        return next(iter(self._lista))

    def esta_vacia(self):
        return self._lista.esta_vacia()


class ColaReproduccion:
    def __init__(self):
        self._cola = Cola()

    def encolar_cancion(self, cancion):
        self._cola.encolar(cancion)

    def siguiente(self):
        return self._cola.desencolar()

    def que_sigue(self):
        return self._cola.ver_frente()


# TEORIA
# El primer siguiente() devuelve Jijiji. La cola es FIFO (primero en entrar,
# primero en salir). Se diferencia de la pila del ejercicio 5 en que esta
# devuelve primero lo ultimo que entro (De Musica Ligera), mientras que la
# cola respeta el orden de llegada y devuelve primero lo mas antiguo.