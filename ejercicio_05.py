from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    pass


class Pila:
    def __init__(self):
        self._items = ListaEnlazada()

    def esta_vacia(self):
        return self._items.esta_vacia()

    def apilar(self, dato):
        self._items.insertar_al_inicio(dato)

    def desapilar(self):
        if self._items.esta_vacia():
            raise PilaVaciaError("La pila está vacía")
        return self._items.quitar_primero()

    def ver_tope(self):
        if self._items.esta_vacia():
            raise PilaVaciaError("La pila está vacía")
        for item in self._items:
            return item


class HistorialAcciones:
    def __init__(self):
        self._pila = Pila()

    def registrar(self, accion):
        self._pila.apilar(accion)

    def deshacer(self):
        return self._pila.desapilar()

    def ultima(self):
        return self._pila.ver_tope()


# TEORIA: Queda "B" en el tope (porque sale "C") y la disciplina se llama LIFO.
