from ejercicio_02.py import RecetaNoEncontrada

class Nodo :
    def __init__(self,dato): 
        self.dato = dato
        self.siguiente = None 

class ListaEnlazada :
    def __init__(self) :
        self._cabeza = None 
        self._cola = None
        self._tamanio = 0

    def Esta_Vacia(self) :
        return self._tamanio == 0

    def tamanio(self) :
        return self._tamanio

    def insertar_al_final(self,dato) :
        nuevo= Nodo(dato) 
        if self.Esta_Vacia() :
            self._cabeza = nuevo
            self._cola = nuevo

        else :
            self._cola.siguiente = nuevo
            self._cola = nuevo
        self._tamanio += 1

    def quitar_rimero(self) :
        if self._esta_vacia () : 
            raise IndexError("La lista esta vacia")
        dato = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente
        self._tamanio -= 1
        if self._tamanio == 0 :
            self._cola= None
        return dato

    def __iter__(self) :
        actual= self._cabeza
        while actual is not None :
            yield actual.daato
            actual= actual.siguiente 


class MenuSemanal :
    dias_validos : ( "lunes", "martes", "miercoles", "jueves",
        "viernes", "sabado", "domingo" )

    def __init__(self) :
        self._menu = ListaEnlazada()    
    
    def agregar(self, dia, receta) :
        if dia not in self.dias_validos:
            raise ValueError(f"Día inválido: {dia}")

        for nodo in self._menu.iter_nodos():
            dia_existente, _ = nodo.dato
            if dia_existente == dia :
                nodo.dato = (dia, receta)
                return

        self._menu.insertar_al_final((dia, receta))

    def quitar (self,dia) :
        receta_quitada = None

        def coincide(par) :
            nonlocal receta_quitada
            if par[0] == dia :
                receta_quitada = par[1]
                return True
            return False

        if not self._menu.eliminar_donde(coincide):
            raise RecetaNoEncontrada(f"No hay receta para {dia}")
        return receta_quitada       

    def receta_de(self, dia):
        for dia_guardado, receta in self._menu :
            if dia_guardado == dia:
                return receta
        raise RecetaNoEncontrada(f"No hay receta para {dia}")

    def __iter__(self):
        return iter(self._menu)    


# TEORIA: la referencia no esta guardada directamente, hace falta recorrer la lista, entonces la referencia al penultimo esta en el antepenultimo