from ejercicio_04 import ListaEnlazada 

class PilaVaciaError(Exception) :
    pass

class pila : 
    def __init__(self):
        self._datos = ListaEnlazada()

    def esta_vacia(self) :
        return self._datos.esta_vacia()

    def apilar(self, dato) :
        self._datos.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar de una pila vacia")

        return self._datos.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia () :
            raise PilaVaciaError("La pila esta vacia")

        for dato in self._datos:
            return dato

class HistorialCcocinado : 
    def __init__(self):
        self._pila = Pila ()

    def cocinar(self, receta) :
        self._pila.apilar(receta)

    def deshacer(self) :
        return self._pila.desapilar()

    def ultima(self) :
        return self._pila.ver_tope ()            

# TEORIA : En el tope queda "B", esto es un lifo        