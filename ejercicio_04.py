class CancionNoEncontradaError(Exception):
    def __init__(self , cancion_id):
        super().__init__(f"no existe cancion con  el id {cancion_id}")

class Nodo:
    def __init__(self , dato , siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada: 
    def __init__(self):
        self.cabeza = None 
        self.cant = 0 
    def esta_vacia(self):
        return self.cabeza is None
    def tamanio(self):
        return self.cant
    def insertar_al_inicio(self, dato):
        nuevo = Nodo (dato , self.cabeza)
        self.cabeza = nuevo
        self.cant += 1
    def insertar_al_final(self, dato):
        nuevo = Nodo(dato None)
        if self.cabeza is None:
            self.cabeza = nuevo
        else: 
            actual =self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.cant += 1
    def quitar_primero(self):
        if self.cabeza is None:
            raise IndexError ("la lista esta vacia")
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        self.cant -=1
        return dato
    def __iter__(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual.siguiente
class Playlist:
    def __init__(self):
        self.canciones = ListaEnlazada() 
    def agregar(self, cancion):
        self.canciones.insertar_al_final(cancion)
    def quitar (self , id):
        nueva_lista = ListaEnlazada()
        encontrada = False
        for  cancion in self.canciones:
            if cancion.id == id and not encontrada:
                encontrada = True
            else:
                nueva_lista.insertar_al_final(cancion)
        if not encontrada :
            raise CancionNoEncontradaError("cancion no encontrada")
        self.canciones = nueva_lista
    def listar(self):
        resu= []
        for cancion in self.canciones:
            resu.append(str(cancion))
            return resu

    def duracion_total(self):
        total = 0
        for cancion in self.canciones:
            total += cancion.duracion_seg
            return total
 #teoria: si la lista selo guarda una referencia al 
# primer nodo y hay n elemento, para insertar al final se recorren n nodos 