# ejercicio_04.py
from ejercicio_02 import CancionNoEncontradaError


class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__(self):
        self._primero = None
        self._tamanio = 0

    def esta_vacia(self) -> bool:
        return self._primero is None

    def tamanio(self) -> int:
        return self._tamanio

    def insertar_al_inicio(self, dato):
        self._primero = Nodo(dato, self._primero)
        self._tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self._primero is None:
            self._primero = nuevo
        else:
            actual = self._primero
            while actual.siguiente is not None:   # recorre los n nodos existentes
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def quitar_primero(self):
        """Devuelve el dato del frente y lo saca de la lista."""
        if self._primero is None:
            raise IndexError("La lista está vacía.")
        dato = self._primero.dato
        self._primero = self._primero.siguiente
        self._tamanio -= 1
        return dato

    def eliminar(self, dato) -> bool:
        """Auxiliar: saca la primera aparición de dato (compara con ==)."""
        anterior = None
        actual = self._primero
        while actual is not None:
            if actual.dato == dato:
                if anterior is None:
                    self._primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def __iter__(self):
        actual = self._primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Playlist:
    """Sin tope de cantidad."""

    def __init__(self):
        self._canciones = ListaEnlazada()

    def agregar(self, cancion):
        self._canciones.insertar_al_final(cancion)

    def quitar(self, id):
        for c in self._canciones:
            if c.id == id:
                self._canciones.eliminar(c)   # Cancion.__eq__ compara por id
                return c
        raise CancionNoEncontradaError(
            f"No existe una canción con id {id} en la playlist."
        )

    def listar(self):
        return [str(c) for c in self._canciones]

    def duracion_total(self):
        total = 0
        for c in self._canciones:
            total += c.duracion_seg
        return total

#Como la lista solo guarda el primer nodo, para insertar al final hay que recorrerla entera hasta 
#encontrar el último nodo: se recorren n nodos (el último es el que tiene siguiente is None), así que
#la operación es O(n). Insertar al inicio, en cambio, es O(1).
