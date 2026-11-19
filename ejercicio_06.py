from ejercicio_01 import Cancion
from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    pass


class Cola:
    def __init__(self):
        self.lista = ListaEnlazada()

    def encolar(self, dato):
        self.lista.insertar_al_final(dato)      

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía")
        return self.lista.quitar_primero()      

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía")
        return self.lista.primero.dato

    def esta_vacia(self):
        return self.lista.esta_vacia()


class ColaReproduccion:
    def __init__(self):
        self.cola = Cola()

    def encolar_cancion(self, cancion):
        self.cola.encolar(cancion)

    def siguiente(self):
        return self.cola.desencolar()

    def que_sigue(self):
        return self.cola.ver_frente()


if __name__ == "__main__":
    c = ColaReproduccion()
    c.encolar_cancion(Cancion(12, "Jijiji", "Patricio Rey", "Un baión", "Rock", 1988, 316))
    c.encolar_cancion(Cancion(20, "Alfonsina y el mar", "Mercedes Sosa", "Mujeres argentinas", "Folklore", 1969, 297))
    c.encolar_cancion(Cancion(30, "De Música Ligera", "Soda Stereo", "Canción animal", "Rock", 1990, 214))

    print(c.que_sigue())    
    print(c.siguiente())    
    print(c.siguiente())    
    print(c.que_sigue())    
    print(c.siguiente())    

    try:
        c.siguiente()
    except ColaVaciaError as e:
        print("Error:", e)  

# TEORÍA:
# El primer siguiente() devuelve "Jijiji", porque la cola es FIFO (el primero
# en entrar es el primero en salir): fue la primera encolada y está al frente.
# En la pila del ejercicio 5 (LIFO) el orden es el inverso: con las mismas tres
# canciones, el primer anterior() devolvía "De Música Ligera", la última en entrar.