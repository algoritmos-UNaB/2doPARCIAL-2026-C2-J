from ejercicio_01 import Cancion
from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    pass


class Pila:
    def __init__(self):
        self._elementos = ListaEnlazada()

    def apilar(self, dato) -> None:
        self._elementos.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar: la pila está vacía.")
        return self._elementos.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede ver el tope: la pila está vacía.")
        return self._elementos.primero.dato

    def esta_vacia(self) -> bool:
        return self._elementos.esta_vacia()


class HistorialReproduccion:
    def __init__(self):
        self._pila = Pila()

    def registrar(self, cancion: Cancion) -> None:
        self._pila.apilar(cancion)

    def anterior(self) -> Cancion:
        return self._pila.desapilar()

    def ultima(self) -> Cancion:
        return self._pila.ver_tope()


# Teoría:
# El primer anterior() devuelve "De Música Ligera".
# Porque una pila funciona bajo la disciplina LIFO (Last In, First Out: el último
# elemento en entrar es el primero en salir), y "De Música Ligera" fue la última
# canción registrada en el historial.