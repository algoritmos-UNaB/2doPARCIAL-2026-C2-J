from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    pass


class Pila:
    def __init__(self) -> None:
        self._elementos = ListaEnlazada()

    def esta_vacia(self) -> bool:
        return self._elementos.esta_vacia()

    def apilar(self, dato: object) -> None:
        self._elementos.insertar_al_inicio(dato)

    def desapilar(self) -> object:
        if self.esta_vacia():
            raise PilaVaciaError("La pila esta vacia.")
        return self._elementos.quitar_primero()

    def ver_tope(self) -> object:
        if self.esta_vacia():
            raise PilaVaciaError("La pila esta vacia.")
        assert self._elementos.cabeza is not None
        return self._elementos.cabeza.dato


class HistorialAcciones:
    def __init__(self) -> None:
        self._acciones = Pila()

    def registrar(self, accion: str) -> None:
        self._acciones.apilar(str(accion))

    def deshacer(self) -> str:
        return str(self._acciones.desapilar())

    def ultima(self) -> str:
        return str(self._acciones.ver_tope())


# TEORIA: Queda "B" en el tope, y esta disciplina se llama LIFO (Last-In, First-Out: el ultimo elemento en entrar es el primero en salir)