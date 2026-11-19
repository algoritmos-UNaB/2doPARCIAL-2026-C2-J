# ejercicio_07.py
from ejercicio_02 import CancionNoEncontradaError

CAMPOS_VALIDOS = ("titulo", "artista", "genero")


def busqueda_lineal(canciones, campo, valor) -> list:
    """Todas las canciones cuyo campo es igual a valor, en el orden original."""
    if campo not in CAMPOS_VALIDOS:
        raise ValueError(
            f"Campo inválido: {campo!r}. Debe ser 'titulo', 'artista' o 'genero'."
        )
    encontradas = []
    for c in canciones:
        if getattr(c, campo) == valor:
            encontradas.append(c)
    return encontradas


def busqueda_binaria_por_titulo(canciones_ordenadas, titulo):
    """Requiere la lista ordenada alfabéticamente por titulo.
    Si hay títulos repetidos, devuelve la primera que encuentre la búsqueda."""
    izq, der = 0, len(canciones_ordenadas) - 1
    while izq <= der:
        medio = (izq + der) // 2
        candidata = canciones_ordenadas[medio]
        if candidata.titulo == titulo:
            return candidata
        elif candidata.titulo < titulo:
            izq = medio + 1
        else:
            der = medio - 1
    raise CancionNoEncontradaError(
        f"No existe una canción con el título {titulo!r}."
    )

"""busqueda_binaria_por_titulo pide la lista ordenada por título porque en cada paso compara con el elemento del medio y descarta 
una mitad entera, esto es valido si todo lo que está a la izquierda es menor y todo lo que está a la derecha es mayor. 
En una lista desordenada podría descartar justo la mitad donde está el título y dar un falso “no encontrado”. La binaria es 
O(log n), porque el rango se divide a la mitad en cada comparación, y la búsqueda lineal por artista es O(n), porque en el peor 
caso revisa las n canciones (y siempre las recorre todas, ya que devuelve todas las coincidencias)."""

