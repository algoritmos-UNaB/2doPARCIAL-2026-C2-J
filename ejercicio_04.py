from ejercicio_01 import Cancion
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
        self._cantidad = 0

    def esta_vacia(self) -> bool:
        return self.primero is None

    def tamanio(self) -> int:
        return self._cantidad

    def insertar_al_inicio(self, dato):
        self.primero = Nodo(dato, self.primero)
        self._cantidad += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:  
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._cantidad += 1

    def quitar_primero(self):
        if self.esta_vacia():
            raise ListaVaciaError("La lista está vacía")
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        self._cantidad -= 1
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

    def quitar(self, id):
        anterior = None
        actual = self.canciones.primero
        while actual is not None:
            if actual.dato.id == id:
                if anterior is None:                    
                    return self.canciones.quitar_primero()
                anterior.siguiente = actual.siguiente    
                self.canciones._cantidad -= 1
                return actual.dato
            anterior = actual
            actual = actual.siguiente
        raise CancionNoEncontradaError(f"La canción {id} no está en la playlist")

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


if __name__ == "__main__":
    p = Playlist()
    print(p.duracion_total())   

    p.agregar(Cancion(12, "Jijiji", "Patricio Rey", "Un baión", "Rock", 1988, 316))
    p.agregar(Cancion(7, "Muchacha", "Spinetta", "Artaud", "Rock", 1973, 186))
    p.agregar(Cancion(61, "Gracias a la Vida", "Violeta Parra", "Últimas", "Folklore", 1966, 270))

    for linea in p.listar():
        print(linea)
    print(p.duracion_total())   

    p.quitar(7)                 
    print(p.listar())
    print(p.canciones.tamanio())  

    try:
        p.quitar(99)
    except CancionNoEncontradaError as e:
        print("Error:", e)

# TEORÍA:
# Como la lista solo guarda una referencia al primer nodo, para insertar al
# final hay que recorrer los n nodos desde el primero hasta llegar al último
# y recién ahí enganchar el nuevo. Es decir, se recorren n nodos: costo O(n).