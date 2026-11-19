class ColaVaciaError(Exception):
    pass

class Cola:
    def __init__(self):
        self._lista = ListaEnlazada()

    def esta_vacia(self) -> bool:
        return self._lista.esta_vacia()

    def encolar(self, dato):
        self._lista.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola esta vacia.")
        return self._lista.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola esta vacia.")
        return self._lista.primero.dato


class ColaReproduccion:
    def __init__(self):
        self._cola = Cola()

    def encolar_cancion(self, cancion: Cancion):
        self._cola.encolar(cancion)

    def siguiente(self) -> Cancion:
        return self._cola.desencolar()

    def que_sigue(self) -> Cancion:
        return self._cola.ver_frente()

# Rta: El primer siguiente() devuelve "Jijiji". La diferencia fundamental es que la Cola responde a un principio 
#FIFO (First-In, First-Out), donde el primer elemento ingresado es el primero en ser procesado, a diferencia de la Pila 
#(LIFO) que recupera los elementos en orden inverso a su llegada .