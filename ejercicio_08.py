from ejercicio_01 import Cancion


def ordenar_por_anio_seleccion(canciones: list[Cancion]) -> list[Cancion]:
    """Selección. Año de mayor a menor."""
    n = len(canciones)
    for i in range(n - 1):
        indice_max = i
        for j in range(i + 1, n):
            if canciones[j].anio > canciones[indice_max].anio:
                indice_max = j
        if indice_max != i:
            canciones[i], canciones[indice_max] = canciones[indice_max], canciones[i]
    return canciones


def ordenar_por_duracion_insercion(canciones: list[Cancion]) -> list[Cancion]:
    """Inserción. duracion_seg de menor a mayor."""
    for i in range(1, len(canciones)):
        actual = canciones[i]
        j = i - 1
        while j >= 0 and canciones[j].duracion_seg > actual.duracion_seg:
            canciones[j + 1] = canciones[j]
            j -= 1
        canciones[j + 1] = actual
    return canciones


