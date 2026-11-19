class CancionNoEncontradaError(Exception):
    pass

def busqueda_lineal(canciones: list, campo: str, valor) -> list:
    resultado = []
    for cancion in canciones:
        if getattr(cancion, campo, None) == valor:
            resultado.append(cancion)
    return resultado

def busqueda_binaria_por_titulo(canciones_ordenadas: list, titulo: str) -> Cancion:
    inicio = 0
    fin = len(canciones_ordenadas) - 1
    hallado = None

    while inicio <= fin:
        medio = (inicio + fin) // 2
        cancion_medio = canciones_ordenadas[medio]

        if cancion_medio.titulo == titulo:
            hallado = cancion_medio
            # Para garantizar que sea la primera aparicion si hay titulos duplicados
            fin = medio - 1
        elif cancion_medio.titulo < titulo:
            inicio = medio + 1
        else:
            fin = medio - 1

    if hallado is not None:
        return hallado
    raise CancionNoEncontradaError(f"La cancion con titulo '{titulo}' no fue encontrada.")

# Rta: La busqueda binaria requiere que la lista este previamente ordenada por la clave de busqueda (titulo) 
#para poder comparar el elemento medio y descartar la mitad de los elementos en cada paso. Por su parte, la busqueda lineal 
#por artista no requiere orden previo pero debe inspeccionar cada elemento uno a uno.