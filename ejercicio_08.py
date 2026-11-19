# ejercicio_08.py

def ordenar_por_anio_seleccion(canciones) -> list:
    """Selección. Año de mayor a menor. In-place."""
    n = len(canciones)
    for i in range(n - 1):
        pos_max = i
        for j in range(i + 1, n):
            if canciones[j].anio > canciones[pos_max].anio:
                pos_max = j
        canciones[i], canciones[pos_max] = canciones[pos_max], canciones[i]
    return canciones


def ordenar_por_duracion_insercion(canciones) -> list:
    """Inserción. duracion_seg de menor a mayor. In-place."""
    for i in range(1, len(canciones)):
        actual = canciones[i]
        j = i - 1
        while j >= 0 and canciones[j].duracion_seg > actual.duracion_seg:
            canciones[j + 1] = canciones[j]
            j -= 1
        canciones[j + 1] = actual
    return canciones


"""El selección tiene peor caso O(n²), porque siempre hace los dos bucles anidados completos, esté la lista ordenada o no. 
El inserción también tiene peor caso O(n²), que ocurre cuando la lista viene en orden inverso y cada elemento se desplaza hasta 
el principio (en el mejor caso, con la lista ya ordenada, es O(n)). El que conserva el orden relativo de dos canciones con 
la misma clave es el inserción, porque solo desplaza elementos estrictamente mayores y nunca pasa una canción por delante de otra 
con igual clave; el selección no lo hace, porque su intercambio a distancia puede saltar un elemento sobre otros de igual clave."""