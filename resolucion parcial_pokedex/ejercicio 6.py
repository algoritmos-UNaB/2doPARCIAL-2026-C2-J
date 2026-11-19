from ejercicio_01 import Pokemon
from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    pass


class Cola:
    def __init__(self) -> None:
        self._elementos = ListaEnlazada()

    def esta_vacia(self) -> bool:
        return self._elementos.esta_vacia()

    def encolar(self, dato: object) -> None:
        self._elementos.insertar_al_final(dato)

    def desencolar(self) -> object:
        if self.esta_vacia():
            raise ColaVaciaError("La cola esta vacia.")
        return self._elementos.quitar_primero()

    def ver_frente(self) -> object:
        if self.esta_vacia():
            raise ColaVaciaError("La cola esta vacia.")
        assert self._elementos.cabeza is not None
        return self._elementos.cabeza.dato


class ColaTurnos:
    def __init__(self) -> None:
        self._turnos = Cola()

    def encolar(self, pokemon: Pokemon) -> None:
        self._turnos.encolar(pokemon)

    def siguiente(self) -> Pokemon:
        return self._turnos.desencolar()  

    def proximo(self) -> Pokemon:
        return self._turnos.ver_frente()  

# TEORIA: Porque una cola sigue la disciplina FIFO (First-In, First-Out): el primer elemento en entrar es el primero en salir, por lo que A sale antes que B y C, que entro ultimo.