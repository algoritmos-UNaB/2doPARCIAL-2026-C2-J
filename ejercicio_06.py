from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    pass


class Cola:
    def __init__(self):
        self._items = ListaEnlazada()

    def esta_vacia(self):
        return self._items.esta_vacia()

    def encolar(self, dato):
        self._items.insertar_al_final(dato)

    def desencolar(self):
        if self._items.esta_vacia():
            raise ColaVaciaError("La cola está vacía")
        return self._items.quitar_primero()

    def ver_frente(self):
        if self._items.esta_vacia():
            raise ColaVaciaError("La cola está vacía")
        for item in self._items:
            return item


class ColaTurnos:
    def __init__(self):
        self._cola = Cola()

    def encolar(self, pokemon):
        self._cola.encolar(pokemon)

    def siguiente(self):
        return self._cola.desencolar()

    def proximo(self):
        return self._cola.ver_frente()


# TEORIA: Porque una cola funciona como FIFO (primero en entrar, primero en salir), entonces sale A que entró primero y C quedó último.
