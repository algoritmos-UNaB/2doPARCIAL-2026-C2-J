from ejercicio_02 import CancionNoEncontradaError

class ListaVaciaError(Exception):
    pass

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
        self.primero = Nodo(dato, self.primero)
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
            raise ListaVaciaError("La lista está vacía")
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        self._tamanio -= 1
        return dato

    def eliminar(self, dato):
        """Busca y elimina la primera aparición de dato. Devuelve True si lo borró."""
        anterior = None
        actual = self.primero

        while actual is not None:
            if actual.dato == dato:
                if anterior is None:
                    self.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente

        return False

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
        cancion_a_borrar = None
        for cancion in self._canciones:
            if cancion.id == id:
                cancion_a_borrar = cancion
                break
        if cancion_a_borrar is None:
            raise CancionNoEncontradaError(f"No se encontró la canción con id {id}")

        self._canciones.eliminar(cancion_a_borrar)

    def listar(self):
        resultado = []
        for cancion in self._canciones:
            resultado.append(str(cancion))
        return resultado

    def duracion_total(self):
        total = 0
        for cancion in self._canciones:
            total += cancion.duracion_seg
        return total

# TEORÍA
# Se recorren los n nodos que ya están en la lista (haciendo n - 1 saltos 
# de puntero hasta llegar al último nodo para enlazar el nuevo). 
# Por lo tanto, la complejidad temporal de insertar al final es O(n).
