from ejercicio_04 import ListaEnlazada

class ColaVaciaError(Exception):
    """Se intenta desencolar o ver el frente de una cola vacia."""

    def __init__(self, mensaje="La cola esta vacia"):
        super().__init__(mensaje)

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
        return self._lista.ver_primero()

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
# El primer siguiente() devuelve "Jijiji". La cola es FIFO (el primero en entrar
# es el primero en salir), asi que sale en el mismo orden en que se encolo. La
# pila del ejercicio 5 es LIFO: con los mismos tres elementos el primero en
# salir era el ultimo registrado (De Musica Ligera).
