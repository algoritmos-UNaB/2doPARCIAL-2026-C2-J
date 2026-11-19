"""## Ejercicio 5 — Historial de reproducción (10 pts)

Implementar `Pila` sobre `ListaEnlazada` (apilar y desapilar en el extremo del primer nodo):

- `apilar(dato)`
- `desapilar()` devuelve el tope. Si está vacía, lanza `PilaVaciaError`.
- `ver_tope()` devuelve el tope y lo deja en la pila. Si está vacía, lanza `PilaVaciaError`.
- `esta_vacia()`

Definir `HistorialReproduccion`, que usa una `Pila` de canciones:

- `registrar(cancion)` apila lo que acaba de sonar.
- `anterior()` desapila y devuelve la canción a la que se vuelve.
- `ultima()` devuelve la última canción reproducida, sin sacarla.

**Teoría.** Se registran, en este orden, Jijiji, Alfonsina y el mar, y De Música Ligera. ¿Qué devuelve el primer `anterior()`? ¿Por qué?

---"""
class PilaVaciaError(Exception):
   def __init__(self, mensaje: str = "La pila eeta vacia."):
        super().__init__(mensaje)

class Pila:
    def __init__(self, lista: "ListaEnlazada | None" = None):
        self._lista = lista if lista is not None else ListaEnlazada()
    def esta_vacia(self) -> bool:  
        return self._lista.esta_vacia()
    def apilar(self, dato) -> None:
        self._lista.insertar_al_frente(dato)
    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar: la pila esta vacia")
        return self._lista.eliminar_del_frente()
    def ver_tope(self): 
        if self.esta_vacia():
            raise PilaVaciaError("No se puede ver el tope: la pila esta vacia")
        return self._lista.ver_frente()


class HistorialReproduccion:
    def __init__(self, pila: Pila | None = None):
        self._pila = pila if pila is not None else Pila()
    def registrar(self, cancion) -> None:
        self._pila.apilar(cancion)
    def anterior(self):
        try:
            return self._pila.desapilar()
        except PilaVaciaError as exc:
            raise PilaVaciaError("No hay canciones anteriores en el historial.") from exc
    def ultima(self):
        try:
            return self._pila.ver_tope()
        except PilaVaciaError as exc:
            raise PilaVaciaError("El historial de reproducciOn estA vacIo.") from exc

"""TEORIA: Devuelve "De MUsica Ligera".
La pila es LIFO, es decir que al registrar en orden Jijiji, 
Alfonsina y el mar y De MUSica Ligera, esta Ultima queda en el tope (el primer nodo de la lista). 
Como anterior() desapila, extrae y devuelve ese tope en O(1)."""         