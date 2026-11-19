class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self._tamanio = 0

    def esta_vacia(self) -> bool:
        return self.primero is None

    def tamanio(self) -> int:
        return self._tamanio

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato, self.primero)
        self.primero = nuevo
        self._tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def quitar_primero(self):
        if self.esta_vacia():
            raise IndexError("Lista vacia.")
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        self._tamanio -= 1
        return dato

    def __iter__(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Playlist:
    def __init__(self):
        self._lista = ListaEnlazada()

    def agregar(self, cancion: Cancion):
        self._lista.insertar_al_final(cancion)

    def quitar(self, id: int):
        if self._lista.esta_vacia():
            raise CancionNoEncontradaError(f"La cancion con ID {id} no esta en la playlist.")

        actual = self._lista.primero
        anterior = None

        while actual is not None and actual.dato.id != id:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            raise CancionNoEncontradaError(f"La cancion con ID {id} no esta en la playlist.")

        if anterior is None:
            self._lista.quitar_primero()
        else:
            anterior.siguiente = actual.siguiente
            self._lista._tamanio -= 1

    def listar(self) -> list:
        return [str(cancion) for cancion in self._lista]

    def duracion_total(self) -> int:
        return sum(cancion.duracion_seg for cancion in self._lista)

# Rta teoria: Al mantener unicamente una referencia al primer nodo, para insertar un elemento al final es 
# necesario recorrer los nodos existentes secuencialmente hasta alcanzar el ultimo nodo y actualizar su atributo siguiente. 
#Por lo tanto, se recorren exactamente n nodos.