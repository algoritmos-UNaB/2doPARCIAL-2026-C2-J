from ejercicio_02 import PokemonNoEncontrado


class EquipoLlenoError(Exception):
    pass


class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__(self):
        self._cabeza = None
        self._tamanio = 0

    def esta_vacia(self):
        return self._cabeza is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato, self._cabeza)
        self._cabeza = nuevo
        self._tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self._cabeza is None:
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def quitar_primero(self):
        if self._cabeza is None:
            raise IndexError("La lista está vacía")
        dato = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente
        self._tamanio -= 1
        return dato

    def eliminar(self, id):
        anterior = None
        actual = self._cabeza
        while actual is not None:
            if actual.dato.id == id:
                if anterior is None:
                    self._cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar(self, id):
        actual = self._cabeza
        while actual is not None:
            if actual.dato.id == id:
                return actual.dato
            actual = actual.siguiente
        return None

    def __iter__(self):
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Equipo:
    MAX_POKEMON = 6

    def __init__(self):
        self._pokemones = ListaEnlazada()

    def agregar(self, pokemon):
        if self._pokemones.tamanio() >= self.MAX_POKEMON:
            raise EquipoLlenoError("El equipo ya tiene el máximo de 6 Pokémon")
        self._pokemones.insertar_al_final(pokemon)

    def quitar(self, id):
        eliminado = self._pokemones.eliminar(id)
        if not eliminado:
            raise PokemonNoEncontrado(f"No se encontró el Pokémon con id {id} en el equipo")

    def cantidad(self):
        return self._pokemones.tamanio()

    def __iter__(self):
        return iter(self._pokemones)


# TEORIA: En una lista simple la referencia al penúltimo está en el siguiente del nodo anterior a él (o en la cabeza si hay solo dos), y como solo se avanza hacia adelante hay que recorrer desde el inicio.
