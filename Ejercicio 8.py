def ordenar_por_anio_seleccion(canciones):
    """Seleccion. Anio de mayor a menor."""
    n = len(canciones)
    for i in range(n - 1):
        indice_mayor = i
        for j in range(i + 1, n):
            if canciones[j].anio > canciones[indice_mayor].anio:
                indice_mayor = j
        if indice_mayor != i:
            canciones[i], canciones[indice_mayor] = canciones[indice_mayor], canciones[i]
    return canciones

def ordenar_por_duracion_insercion(canciones):
    """Insercion. duracion_seg de menor a mayor."""
    for i in range(1, len(canciones)):
        actual = canciones[i]
        j = i - 1
        # Comparacion estricta (>): no pasa por encima de claves iguales (estable).
        while j >= 0 and canciones[j].duracion_seg > actual.duracion_seg:
            canciones[j + 1] = canciones[j]
            j -= 1
        canciones[j + 1] = actual
    return canciones

# TEORIA
# Peor caso de ambos: O(n^2).
#  - Seleccion: siempre hace ~n^2/2 comparaciones (busca el mayor en el resto
#  de la lista), tambien en el mejor caso.
#  - Insercion: en el peor caso (lista en orden inverso) cada elemento se
#  desplaza hasta el principio; en el mejor caso (ya ordenada) es O(n).
# El que conserva el orden relativo de claves iguales (estable) es el de
# insercion. La seleccion no es estable: el intercambio a distancia puede pasar
# un elemento por encima de otro con la misma clave.
