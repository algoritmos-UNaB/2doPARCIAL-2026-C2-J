from ejercicio_02 import CancionNoEncontradaError

CAMPOS_VALIDOS = ("titulo", "artista", "genero")

def busqueda_lineal(canciones, campo, valor):
    if campo not in CAMPOS_VALIDOS:
        raise ValueError(f"Campo invalido: {campo!r}. Debe ser uno de {CAMPOS_VALIDOS}")
    encontradas = []
    for cancion in canciones:
        if getattr(cancion, campo) == valor:
            encontradas.append(cancion)
    return encontradas

def busqueda_binaria_por_titulo(canciones_ordenadas, titulo):
    inferior = 0
    superior = len(canciones_ordenadas) - 1
    while inferior <= superior:
        medio = (inferior + superior) // 2
        titulo_medio = canciones_ordenadas[medio].titulo
        if titulo_medio == titulo:
            return canciones_ordenadas[medio]
        if titulo_medio < titulo:
            inferior = medio + 1
        else:
            superior = medio - 1
    raise CancionNoEncontradaError(f"No existe una cancion con titulo {titulo!r}")

# TEORIA
# La busqueda binaria compara con el elemento del medio y descarta la mitad
# donde el titulo no puede estar. Eso solo es valido si la lista esta ordenada
# por titulo: si no lo esta, descartar una mitad puede eliminar justo donde
# esta el titulo buscado.
# Complejidad: la binaria es O(log n) sobre n canciones. La lineal por artista
# es O(n), porque en el peor caso recorre todas las canciones (ademas hay que
# recorrerlas todas, ya que devuelve todas las coincidencias).
