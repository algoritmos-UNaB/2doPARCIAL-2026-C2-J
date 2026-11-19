from ejercicio_01 import Cancion
from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    pass


class Pila:
    def __init__(self):
        self.lista = ListaEnlazada()

    def apilar(self, dato):
        self.lista.insertar_al_inicio(dato)    

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía")
        return self.lista.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía")
        return self.lista.primero.dato

    def esta_vacia(self):
        return self.lista.esta_vacia()


class HistorialReproduccion:
    def __init__(self):
        self.pila = Pila()

    def registrar(self, cancion):
        self.pila.apilar(cancion)

    def anterior(self):
        return self.pila.desapilar()

    def ultima(self):
        return self.pila.ver_tope()


if __name__ == "__main__":
    h = HistorialReproduccion()
    h.registrar(Cancion(12, "Jijiji", "Patricio Rey", "Un baión", "Rock", 1988, 316))
    h.registrar(Cancion(20, "Alfonsina y el mar", "Mercedes Sosa", "Mujeres argentinas", "Folklore", 1969, 297))
    h.registrar(Cancion(30, "De Música Ligera", "Soda Stereo", "Canción animal", "Rock", 1990, 214))

    print(h.ultima())      
    print(h.anterior())     
    print(h.anterior())     
    print(h.ultima())       
    print(h.anterior())     

    try:
        h.anterior()
    except PilaVaciaError as e:
        print("Error:", e)  

# TEORÍA:
# El primer anterior() devuelve "De Música Ligera", porque la pila es LIFO
# (el último en entrar es el primero en salir): fue la última registrada,
# así que quedó en el tope, y desapilar siempre saca el tope.