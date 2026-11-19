from Ejercicio4_recetario import ListaEnlazada


class PilaVaciaError(Exception):
    pass


class Pila:
    def __init__(self):
        self._lista = ListaEnlazada()

    def apilar(self, dato):
        self._lista.insertar_al_inicio(dato)

    def desapilar(self):
        if self._lista.esta_vacia():
            raise PilaVaciaError("La pila está vacía")
        return self._lista.quitar_primero()

    def ver_tope(self):
        if self._lista.esta_vacia():
            raise PilaVaciaError("La pila está vacía")
        return self._lista.primero.dato

    def esta_vacia(self):
        return self._lista.esta_vacia()


class HistorialCocinado:
    def __init__(self):
        self._pila = Pila()

    def cocinar(self, receta):
        self._pila.apilar(receta)

    def deshacer(self):
        return self._pila.desapilar()

    def ultima(self):
        return self._pila.ver_tope()


# TEORIA
# Queda "B" en el tope.
# Esta disciplina se llama LIFO (último en entrar, primero en salir)..