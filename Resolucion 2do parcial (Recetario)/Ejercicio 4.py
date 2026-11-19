from ejercicio_02 import RecetaNoEncontrada

DIAS_VALIDOS = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")


class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self._tamanio = 0

    def esta_vacia(self):
        return self.primero is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_inicio(self, dato):
        self.primero = Nodo(dato, self.primero)
        self._tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def quitar_primero(self):
        if self.primero is None:
            raise IndexError("La lista está vacía.")
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        self._tamanio -= 1
        return dato

    def eliminar_donde(self, condicion):
        anterior = None
        actual = self.primero
        while actual is not None:
            if condicion(actual.dato):
                if anterior is None:
                    self.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def __iter__(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class MenuSemanal:
    def __init__(self):
        self.items = ListaEnlazada()

    def agregar(self, dia, receta):
        if dia not in DIAS_VALIDOS:
            raise ValueError(f"Día inválido: {dia}")
        actual = self.items.primero
        while actual is not None:
            if actual.dato[0] == dia:
                actual.dato = (dia, receta)
                return
            actual = actual.siguiente
        self.items.insertar_al_final((dia, receta))

    def quitar(self, dia):
        eliminado = self.items.eliminar_donde(lambda par: par[0] == dia)
        if not eliminado:
            raise RecetaNoEncontrada(f"No hay receta asignada para {dia}.")

    def receta_de(self, dia):
        for d, receta in self.items:
            if d == dia:
                return receta
        raise RecetaNoEncontrada(f"No hay receta asignada para {dia}.")

    def __iter__(self):
        return iter(self.items)


# TEORIA: En una lista enlazada simple esa referencia únicamente está guardada en el atributo siguiente del nodo antepenúltimo, por lo que no existe acceso directo y hay que recorrer la lista desde el primer nodo hasta encontrar el nodo cuyo siguiente.siguiente sea None.