from ejercicio_01 import Cancion
from ejercicio_04 import ListaEnlazada

class PilaVaciaError(Exception):
    pass


class Pila:
    def __init__(self):
        self.elementos = ListaEnlazada()
    def apilar(self, dato):
        self.elementos.insertar_al_inicio(dato)
    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError('No se puede desapilar, la pila esta vacia')
        return self.elementos.quitar_primero()
    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError('No se puede ver el tope la pila esta vacia')
        return self.elementos.primero.dato
    def esta_vacia(self):
        return self.elementos.esta_vacia()


class HistorialReproduccion:
    def __init__(self):
        self.pila = Pila()
    def registrar(self, cancion):
        self.pila.apilar(cancion)
    def anterior(self):
        return self.pila.desapilar()
    def ultima(self):
        return self.pila.ver_tope()


"""
Si se registran en el orden dado, el primer anterior devuelve "De Musica Ligera". en las pilas el ultimo elemento ingresado queda en el tope. Al llamar a anterior() el metodo desapilar() extrae y retorna la cancion que se encuentra en lo mas alto, que sería la ultima que fue registrada.

"""