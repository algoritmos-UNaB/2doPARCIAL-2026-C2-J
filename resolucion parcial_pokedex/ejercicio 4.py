from ejercicio_01 import Pokemon
from ejercicio_02 import PokemonNoEncontrado


class EquipoLlenoError(Exception):
    pass


class Nodo:
    def __init__(self, dato: object, siguiente: "Nodo | None" = None) -> None:
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__(self) -> None:
        self.cabeza: Nodo | None = None
        self._tamanio: int = 0

    def esta_vacia(self) -> bool:
        return self.cabeza is None

    def tamanio(self) -> int:
        return self._tamanio

    def insertar_al_inicio(self, dato: object) -> None:
        self.cabeza = Nodo(dato, self.cabeza)
        self._tamanio += 1

    def insertar_al_final(self, dato: object) -> None:
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def quitar_primero(self) -> object:
        if self.cabeza is None:
            raise IndexError("La lista enlazada esta vacia.")
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        self._tamanio -= 1
        return dato

    def eliminar(self, id: int) -> bool:
        anterior: Nodo | None = None
        actual = self.cabeza

        while actual is not None:
            if getattr(actual.dato, "id", None) == id:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente

        return False

    def buscar(self, id: int) -> object | None:
        actual = self.cabeza
        while actual is not None:
            if getattr(actual.dato, "id", None) == id:
                return actual.dato
            actual = actual.siguiente
        return None

    def __iter__(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Equipo:
    MAX_POKEMON = 6

    def __init__(self) -> None:
        self._pokemones = ListaEnlazada()

    def agregar(self, pokemon: Pokemon) -> None:
        if self._pokemones.tamanio() >= self.MAX_POKEMON:
            raise EquipoLlenoError("El equipo ya tiene el maximo de 6 Pokemon.")
        self._pokemones.insertar_al_final(pokemon)

    def quitar(self, id: int) -> None:
        eliminado = self._pokemones.eliminar(id)
        if not eliminado:
            raise PokemonNoEncontrado(f"No se encontro ningun Pokemon con id {id} en el equipo.")

    def cantidad(self) -> int:
        return self._pokemones.tamanio()

    def __iter__(self):
        return iter(self._pokemones)


# TEORIA: En una lista enlazada simple no esta guardada en ningun atributo especial, sino que se descubre recorriendo desde la cabeza hasta el nodo cuyo siguiente.siguiente sea None. Ese nodo encontrado es el penultimo y su atributo siguiente apunta al ultimo nodo