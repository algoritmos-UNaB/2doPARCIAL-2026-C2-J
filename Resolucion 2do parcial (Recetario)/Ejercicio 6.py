from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    """Se intentó desencolar o ver el frente de una cola vacía."""

    def __init__(self, mensaje="La cola está vacía"):
        super().__init__(mensaje)


class Cola:
    """Cola (FIFO) apoyada en una ListaEnlazada: el frente es el primer nodo."""

    def __init__(self):
        self._datos = ListaEnlazada()

    def encolar(self, dato):
        self._datos.insertar_al_final(dato)

    def desencolar(self):
        if self._datos.esta_vacia():
            raise ColaVaciaError()
        return self._datos.quitar_primero()

    def ver_frente(self):
        if self._datos.esta_vacia():
            raise ColaVaciaError()
        return next(iter(self._datos))

    def esta_vacia(self):
        return self._datos.esta_vacia()


class ColaPreparacion:
    """Recetas pendientes de preparar, usando una Cola de Receta."""

    def __init__(self):
        self._cola = Cola()

    def encolar(self, receta):
        self._cola.encolar(receta)

    def siguiente(self):
        return self._cola.desencolar()

    def proxima(self):
        return self._cola.ver_frente()


# TEORIA
# No devuelve C porque la cola es FIFO (First In, First Out): desencolar
# saca el elemento que lleva más tiempo esperando, es decir el primero que
# entró (A), mientras que C, al ser el último en entrar, es el último en salir.
