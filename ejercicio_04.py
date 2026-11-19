from ejercicio_01 import Cancion

class CancionNoEncontradaError(Exception):
    pass

class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.cantidad = 0

    def esta_vacia(self) -> bool:
        return self.primero is None
    def tamanio(self) -> int: 
        return self.cantidad
    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato, self.primero)
        self.primero = nuevo
        self.cantidad +=1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.cantidad += 1

    def quitar_primero(self):
        if self.esta_vacia():
            raise IndexError('La lista esta vacia')
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        self.cantidad -=1
        return dato
    def __iter__(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Playlist:
    def __init__(self):
        self.canciones = ListaEnlazada()
    def agregar(self, cancion):
        self.canciones.insertar_al_final(cancion)
    def quitar(self, id_cancion):
        if self.canciones.esta_vacia():
            raise CancionNoEncontradaError(f"no existe cancion con id {id_cancion} en la playlist")
        if self.canciones.primero.dato.id == id_cancion:
            return self.canciones.quitar_primero()
        anterior = self.canciones.primero
        actual = self.canciones.primero.siguiente
        while actual is not None:
            if actual.dato.id == id_cancion:
                anterior.siguiente = actual.siguiente
                self.canciones.cantidad  -=1
                return actual.dato
            anterior = actual
            actual = actual.siguiente
        raise CancionNoEncontradaError(f'no existe cancion con id {id_cancion} en la playlist')
    def listar(self):
        resultado = []
        for cancion in self.canciones:
            resultado.append(str(cancion))
        return resultado
    def duracion_total(self):
        total = 0
        for cancion in self.canciones:
            total += cancion.duracion_seg
        return total


"""
Para insertar al final es necesario recorrer los n nodos existentes uno por uno hasta llegar al ultimo donde el puntero siguiente es None.
"""