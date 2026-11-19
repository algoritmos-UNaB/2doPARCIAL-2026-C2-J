from ejercicio_01 import Cancion
from ejercicio_04 import ListaEnlazada

class ColaVaciaError(Exception):
    pass


class Cola:
    def __init__(self):
        self.elementos = ListaEnlazada()
    
    def encolar(self, dato):
        self.elementos.insertar_al_final(dato)
    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError('No se puede desencolar,la cola esta vacia')
        return self.elementos.quitar_primero()
    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("no se puede ver el frente, la cola esta vacia")
        return self.elementos.primero.dato
    def esta_vacia(self):
        return self.elementos.esta_vacia()
    

class ColaReproduccion:
    def __init__(self):
        self.cola = Cola()
    def encolar_cancion(self, cancion):
        self.cola.encolar(cancion)
    def siguiente(self):
        return self.cola.desencolar()
    def que_sigue(self):
        return self.cola.ver_frente()


"""
En el orden dado, el primer siguiente() devuelve Jijiji. La cola entrega los elementos en orden cronologico en el que fueron agregados
"""