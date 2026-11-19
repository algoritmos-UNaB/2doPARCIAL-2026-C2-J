from Ejercicio4_recetario import ListaEnlazada


class ColaVaciaError(Exception):
    pass


class Cola:
    def __init__(self):
        self._lista = ListaEnlazada()

    def encolar(self, dato):
        self._lista.insertar_al_final(dato)

    def desencolar(self):
        if self._lista.esta_vacia():
            raise ColaVaciaError("La cola está vacía")
        return self._lista.quitar_primero()

    def ver_frente(self):
        if self._lista.esta_vacia():
            raise ColaVaciaError("La cola está vacía")
        return self._lista.primero.dato

    def esta_vacia(self):
        return self._lista.esta_vacia()


class ColaPreparacion:
    def __init__(self):
        self._cola = Cola()

    def encolar(self, receta):
        self._cola.encolar(receta)

    def siguiente(self):
        return self._cola.desencolar()

    def proxima(self):
        return self._cola.ver_frente()


# TEORIA
# Porque la cola respeta el orden de llegada:
# el primero en entrar es el primero en salir (FIFO).