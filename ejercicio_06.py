"""
## Ejercicio 6 — Cola de reproducción (10 pts)

Implementar `Cola` sobre `ListaEnlazada`:

- `encolar(dato)` agrega al final.
- `desencolar()` saca y devuelve el primero. Si está vacía, lanza `ColaVaciaError`.
- `ver_frente()` devuelve el primero y lo deja en la cola. Si está vacía, lanza `ColaVaciaError`.
- `esta_vacia()`

Definir `ColaReproduccion` (la cola “up next”), que usa una `Cola` de canciones:

- `encolar_cancion(cancion)`
- `siguiente()` devuelve la canción que toca ahora.
- `que_sigue()` devuelve la canción del frente, sin sacarla.

**Teoría.** Se encolan, en este orden, Jijiji, Alfonsina y el mar, y De Música Ligera. ¿Qué devuelve el primer `siguiente()`? ¿En qué se diferencia este orden del de la pila del ejercicio 5?
"""
class ColaVaciaError(Exception):
    def __init__(self, mensaje: str = "La cola esta vacia."):
        super().__init__(mensaje)


class Cola:
    def __init__(self, lista: "ListaEnlazada | None" = None):
        self._lista = lista if lista is not None else ListaEnlazada()
    def esta_vacia(self) -> bool:
        return self._lista.esta_vacia()
    def encolar(self, dato) -> None:
        self._lista.insertar_al_final(dato)
    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede desencolar: la cola esta vacia.")
        return self._lista.eliminar_del_frente()
    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede ver el frente: la cola esta vacia.")
        return self._lista.ver_frente()

class ColaReproduccion:
    def __init__(self, cola: Cola | None = None):
        self._cola = cola if cola is not None else Cola()
    def encolar_cancion(self, cancion) -> None:
        self._cola.encolar(cancion)
    def siguiente(self):
        try:
            return self._cola.desencolar()
        except ColaVaciaError as exc:
            raise ColaVaciaError("No hay  canciones en la cola de reprod.") from exc
    def que_sigue(self):
         try:
            return self._cola.ver_frente()
        except ColaVaciaError as exc:
            raise ColaVaciaError("La cola de reprod esta vacia.") from exc
"""TEORIA: Devuelve "Jijiji" porque La cola es FIFO : al encolar Jijiji, 
Alfonsina y el mar y De MUsica Ligera, 
"Jijiji" queda al frente y sale primero con siguiente(). 
A diferencia de la pila del ejercicio 5 (LIFO), 
que sacaba el Ultimo elemento , la cola saca el primero."""