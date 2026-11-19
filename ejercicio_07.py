"""- Búsqueda y ordenamiento se escriben a mano. `list.sort`, `sorted` y `bisect` no se toman como resolución de los ejercicios 7 y 8.
- Cada excepción es una clase propia que hereda de `Exception`, con un mensaje que explique el caso. Un `except:` sin tipo no cuenta.
- Los métodos devuelven un valor o lanzan la excepción. Avisar solo con `print` no reemplaza el `return` ni el `raise`.
- Se asume que las versiones no forman ciclos.

## Ejercicio 7 — Búsqueda (10 pts)

Las funciones reciben una `list` de `Cancion`. Se implementan a mano.

```python
def busqueda_lineal(canciones, campo, valor) -> list: ...
def busqueda_binaria_por_titulo(canciones_ordenadas, titulo) -> Cancion: ...
```

- `busqueda_lineal`: `campo` es `"titulo"`, `"artista"` o `"genero"`. Devuelve todas las canciones cuyo campo es igual a `valor`, en el orden original. Si no hay ninguna, lista vacía. `"Rock"` y `"Soda Stereo"` tienen que poder buscarse por este camino.
- Binaria por `titulo`, sobre una lista ya ordenada alfabéticamente por `titulo`. Si el título no está, `CancionNoEncontradaError`. Si hubiera dos canciones con el mismo título, devuelve la primera que encuentre la búsqueda.

**Teoría.** ¿Por qué `busqueda_binaria_por_titulo` pide la lista ordenada por título? ¿Qué complejidad tiene sobre `n` canciones, y qué complejidad tiene la búsqueda lineal por artista?

---

"""
class CancionNoEncontradaError(Exception):
    def __init__(self, mensaje: str = " cancion no encontrada."):
        super().__init__(mensaje)

CAMPOS_VALIDOS = ("titulo", "artista", "genero")


def busqueda_lineal(canciones, campo, valor) -> list:
    if campo not in CAMPOS_VALIDOS:
        raise ValueError(f"Campo invalido '{campo}'. Use uno de: {CAMPOS_VALIDOS}.")
    resultados = []
    for cancion in canciones:
        if cancion.campo == valor:
            resultados.append(cancion)
    return resultados


def busqueda_binaria_por_titulo(canciones_ordenadas, titulo):
    izquierda = 0
    derecha = len(canciones_ordenadas) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = canciones_ordenadas[medio]
        if actual.titulo == titulo:
            return actual
        if actual.titulo < titulo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    raise CancionNoEncontradaError(f"No se encontro ninguna cancion con titulo '{titulo}'.")

"""TEORIA: La busqueda binaria exige que la lista este ordenada por titulo para poder descartar 
la mitad izquierda o derecha comparando con el centro sin perder la cancion buscada.
tiene complejidad  sobre n canciones, mientras que la busqueda lineal por 
artista tiene complejidad porque revisa toda la lista una por una."""