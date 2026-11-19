from ejercicio_04 import ListaEnlazada 

class ColaVaciaError(Exception) :
    pass


class Cola :
    def __init__(self) :
        self._datos = ListaEnlazada()

    def esta_vacia(self) :
        return self._datos.esta_vacia()

    def encolar(self, dato):
        self._datos.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede desencolar de una cola vacia")
        return self._datos.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola esta vacia")

        for dato in self._datos:
            return dato


class ColaPreparacion :
    def __init__(self) :
        self._cola = Cola ()

    def encolar(self, receta):
        self._cola.encolar(receta)

    def siguiente(self):
        return self._cola.desencolar()

    def proxima(self) :
        return self._cola.ver_frente ()


# Teoria : Porque sigue la disciplina fifo, primero entra a y primero sale a