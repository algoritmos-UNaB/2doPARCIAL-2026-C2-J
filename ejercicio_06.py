from ejercicio_01 import Cancion
from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    pass


class Cola:
    def __init__(self):
        self._elementos = ListaEnlazada()

    def encolar(self, dato) -> None:
        self._elementos.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede desencolar: la cola está vacía.")
        return self._elementos.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede ver el frente: la cola está vacía.")
        return self._elementos.primero.dato

    def esta_vacia(self) -> bool:
        return self._elementos.esta_vacia()


class ColaReproduccion:
    def __init__(self):
        self._cola = Cola()

    def encolar_cancion(self, cancion: Cancion) -> None:
        self._cola.encolar(cancion)

    def siguiente(self) -> Cancion:
        return self._cola.desencolar()

    def que_sigue(self) -> Cancion:
        return self._cola.ver_frente()


# Teoría:
# El primer siguiente() devuelve "Jijiji".
# Se diferencia de la pila del ejercicio 5 en que una cola sigue la disciplina
# FIFO (First In, First Out: el primer elemento en entrar es el primero en salir),
# por lo que sale primero lo que se encoló al principio ("Jijiji"), mientras que
# la pila (LIFO) devuelve primero lo último que entró ("De Música Ligera").