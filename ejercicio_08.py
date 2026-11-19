from ejercicio_01 import Cancion


def ordenar_por_anio_seleccion(canciones) -> list:
    """Selección. Año de mayor a menor."""
    n = len(canciones)
    for i in range(n):
        idx_max = i
        for j in range(i+1, n):
            if canciones[j].anio > canciones[idx_max].anio:
                idx_max = j
        canciones[i], canciones[idx_max] = canciones[idx_max]
    return canciones

def ordenar_por_duracion_insercion(canciones) -> list:
    """Inserción. duracion_seg de menor a mayor."""
    n = len(canciones)
    for i in range(1,n):
        actual = canciones[i]
        j = i-1
        while j >= 0 and canciones[j].duracion_seg > actual.duracion_seg:
            canciones[j+1] = canciones[j]
            j -=1
        canciones[j+1] = actual
    return canciones


"""
El ordenamiento de inserción conserva el orden relativo pq solo desplaza elementos estrictamente mayores manteniendo en su posicion relativa previa a aquellos que tengan igual duracion, en cambio el ordenamiento por seleccion es inestable pq realiza intercambios a larga distancia que pueden alterar el orden relativo original.
"""