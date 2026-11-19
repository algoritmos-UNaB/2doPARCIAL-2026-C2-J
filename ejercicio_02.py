"""
---

## Ejercicio 2 — Biblioteca (8 pts)

Definir la clase `Biblioteca`, el catálogo de todas las canciones.

- `agregar(cancion)` incorpora una canción.
- `cantidad()` devuelve cuántas hay.
- `obtener(id)` devuelve la canción con ese `id`. Si no está, lanza `CancionNoEncontradaError`.
- `listar()` devuelve una lista de strings, uno por canción, usando `__str__`.
- `__iter__` permite recorrer las canciones con un `for`.

La playlist no vive en esta clase.

**Teoría.** En una o dos oraciones: qué guarda la biblioteca y qué guarda una playlist.

---
"""

class CancionNoEncontradaError(Exception):
    def __init__(self , id):
        super().__init__(f"no esxiste el id {id}")

class Biblioteca:
    def __init__(self):
        self.canciones = []

    def agregar (self , cancion):
        self.canciones.append(cancion)

    def cantidad(self):
        return len(self.canciones)
    
    def obtener(self , id):
        for i in self.canciones:
            if i.id == id:
                return i
        raise CancionNoEncontradaError(id)
    
    
    def listar(self):
        resu = []
        for i in self.canciones:
            resu.append(str(i))
        return resu
    def __iter__(self):
        return iter(self.canciones)
    
"""TEORIA: la biblioteca guarda todas las canciones del catalogo , 
mientras que la playlist guarda algunas elegidas o que estuviesen en un orden en particular
de la biblioteca
"""