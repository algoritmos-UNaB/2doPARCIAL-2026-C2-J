from ejercicio_02 import CancionNoEncontradaError

class ListaVaciaError(Exception):
    """Se intenta sacar o ver un elemento de una lista vacia."""

    def __init__(self, mensaje="La lista esta vacia"):
        super().__init__(mensaje)

class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self._tamanio = 0

    def esta_vacia(self):
        return self.primero is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_inicio(self, dato):
        self.primero = Nodo(dato, self.primero)
        self._tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def quitar_primero(self):
        if self.primero is None:
            raise ListaVaciaError("No se puede quitar el primero de una lista vacia")
        nodo = self.primero
        self.primero = nodo.siguiente
        self._tamanio -= 1
        return nodo.dato

    def ver_primero(self):
        if self.primero is None:
            raise ListaVaciaError("No hay primer elemento en una lista vacia")
        return self.primero.dato

    def quitar_donde(self, condicion):
        """Quita el primer dato que cumple la condicion y lo devuelve. None si no hay."""
        anterior = None
        actual = self.primero
        while actual is not None:
            if condicion(actual.dato):
                if anterior is None:
                    self.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return actual.dato
            anterior = actual
            actual = actual.siguiente
        return None

    def __iter__(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

class Playlist:
    def __init__(self):
        self._canciones = ListaEnlazada()

    def agregar(self, cancion):
        self._canciones.insertar_al_final(cancion)

    def quitar(self, id):
        quitada = self._canciones.quitar_donde(lambda c: c.id == id)
        if quitada is None:
            raise CancionNoEncontradaError(f"La cancion con id {id} no esta en la playlist")
        return quitada

    def listar(self):
        return [str(cancion) for cancion in self._canciones]

    def duracion_total(self):
        total = 0
        for cancion in self._canciones:
            total += cancion.duracion_seg
        return total

    def __iter__(self):
        return iter(self._canciones)
      
# TEORIA
# Como la lista solo guarda la referencia al primer nodo, para insertar al final
# hay que recorrer los n nodos hasta llegar al ultimo (n nodos, o n-1 saltos
# hasta el ultimo): la operacion es O(n).
