from ejercicio_01 import Cancion
from ejercicio_02 import CancionNoEncontradaError


def busqueda_lineal(canciones: list[Cancion], campo: str, valor) -> list[Cancion]:
    """Busca todas las canciones cuyo atributo `campo` coincida con `valor`."""
    if campo not in ("titulo", "artista", "genero"):
        raise ValueError(f"Campo de búsqueda no válido: {campo}")

    resultados: list[Cancion] = []
    for cancion in canciones:
        if getattr(cancion, campo) == valor:
            resultados.append(cancion)
    return resultados


def busqueda_binaria_por_titulo(canciones_ordenadas: list[Cancion], titulo: str) -> Cancion:
    """Busca una canción por `titulo` en una lista ordenada alfabéticamente por título."""
    izquierda = 0
    derecha = len(canciones_ordenadas) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = canciones_ordenadas[medio]

        if actual.titulo == titulo:
            return actual
        elif actual.titulo < titulo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    raise CancionNoEncontradaError(f"No se encontró ninguna canción con título '{titulo}'.")


# Teoría:
# La búsqueda binaria requiere que la lista esté ordenada por título para poder
# descartar en cada paso la mitad de los elementos según si el título buscado es
# mayor o menor que el elemento central. Sobre n canciones, la búsqueda binaria
# tiene complejidad temporal O(log n) en el peor caso, mientras que la búsqueda
# lineal por artista tiene complejidad temporal O(n) en el peor caso, ya que puede
# requerir revisar todos los elementos de la lista.