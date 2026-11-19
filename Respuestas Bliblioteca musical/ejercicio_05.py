class PilaVaciaError(Exception):
    pass

class Pila:
    def __init__(self):
        self._lista = ListaEnlazada()

    def esta_vacia(self) -> bool:
        return self._lista.esta_vacia()

    def apilar(self, dato):
        self._lista.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")
        return self._lista.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")
        return self._lista.primero.dato


class HistorialReproduccion:
    def __init__(self):
        self._pila = Pila()

    def registrar(self, cancion: Cancion):
        self._pila.apilar(cancion)

    def anterior(self) -> Cancion:
        # Desapila la cancion actual y devuelve la cancion a la que se vuelve
        self._pila.desapilar()
        return self._pila.ver_tope()

    def ultima(self) -> Cancion:
        return self._pila.ver_tope()

# Rta: Al registrar en orden Jijiji, Alfonsina y el mar, y De Musica Ligera, el tope de la pila queda ocupado por
# De Musica Ligera. El primer metodo anterior() desapila De Musica Ligera y devuelve "Alfonsina y el mar". 
#Esto ocurre porque la pila sigue una disciplina LIFO (Last-In, First-Out), sacando el ultimo elemento agregado y dejando 
#como tope la cancion previa