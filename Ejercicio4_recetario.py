from Ejercicio2_recetario import RecetaNoEncontrada

DIAS = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self._tamanio = 0

    def esta_vacia(self):
        return self.primero is None

    def tamanio(self):
        return self._tamanio

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

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.primero
        self.primero = nuevo
        self._tamanio += 1

    def quitar_primero(self):
        if self.primero is None:
            raise IndexError("La lista está vacía")
        nodo = self.primero
        self.primero = nodo.siguiente
        self._tamanio -= 1
        return nodo.dato

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
        self._lista = ListaEnlazada()

    def agregar(self, dia, receta):
        if dia not in DIAS:
            raise ValueError(f"Día inválido: {dia}")
        nodo = self._lista.primero
        while nodo is not None:
            if nodo.dato[0] == dia:
                nodo.dato = (dia, receta)
                return
            nodo = nodo.siguiente
        self._lista.insertar_al_final((dia, receta))

    def quitar(self, dia):
        if not self._lista.eliminar_donde(lambda par: par[0] == dia):
            raise RecetaNoEncontrada(f"No hay receta el día {dia}")

    def receta_de(self, dia):
        for d, receta in self._lista:
            if d == dia:
                return receta
        raise RecetaNoEncontrada(f"No hay receta el día {dia}")

    def __iter__(self):
        return iter(self._lista)


# TEORIA
# La referencia al último nodo está guardada en el atributo siguiente del penúltimo nodo, y los nodos
# no tienen referencia hacia atrás, por eso hay que recorrer la lista desde el primero hasta llegar al penúltimo.