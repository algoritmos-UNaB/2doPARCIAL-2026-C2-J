from ejercicio_01 import Cancion

class CancionNoEncontradaError(Exception):
    pass

def busqueda_lineal(canciones, campo, valor) -> list:
    resultado = []
    for cancoin in canciones:
        if getattr(cancion, campo, None) == valor:
            resultado.append(cancion)
    return resultado


def busqueda_binaria_por_titulo(canciones_ordenadas, titulo) -> Cancion:
    izq = 0
    der = len(canciones_ordenadas) - 1

    while izq <= der:
        medio = (izq + der) // 2
        titulo_actual = canciones_ordenadas[medio].titulo

        if titulo_actual == titulo:
            return canciones_ordenadas[medio]
        elif titulo_actual < titulo:
            izq = medio + 1
        else:
            der = medio - 1
    raise CancionNoEncontradaError(f'No se encontro la cancion con titulo {titulo}')


"""
La busqueda binaria necesita que la lista este ordenada porque en cada paso compara el elemento centro con el buscado para descartar la mitad de la coleccion

La busqueda binaria por titulo tiene una complejidad de O(log n) porque reduce los elementos a la mitad en cada iteracion
La busqueda lineal por artista tiene una complejidad de O(n), porque no requiere ordenamiento y en el peor de los casos revisa los n elementos que estan en la lista.
"""