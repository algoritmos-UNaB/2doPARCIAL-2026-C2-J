""""Ejercicio 8 — Ordenamiento (10 pts)

Ordenar in-place una `list` de `Cancion` y devolver esa misma lista. Dos algoritmos distintos, escritos a mano:

```python
def ordenar_por_anio_seleccion(canciones) -> list:
    #Selección. Año de mayor a menor.

def ordenar_por_duracion_insercion(canciones) -> list:
    #Inserción. duracion_seg de menor a mayor.
```

Con los datos de prueba, el remix (2020) queda antes que el unplugged (1996) al ordenar por año, y De Música Ligera (213 s) queda antes que Jijiji (316 s) al ordenar por duración.

**Teoría.** Dar la complejidad de peor caso de cada algoritmo. ¿Cuál de los dos conserva el orden relativo de dos canciones con la misma clave?
"""
def ordenar_por_anio_seleccion(canciones) -> list:
    n = len(canciones)
    for i in range(n - 1):
        idx_max = i
        for j in range(i + 1, n):
            if canciones[j].anio > canciones[idx_max].anio:
                idx_max = j
        if idx_max != i:
            canciones[i], canciones[idx_max] = canciones[idx_max], canciones[i]
    return canciones


def ordenar_por_duracion_insercion(canciones) -> list:
    for i in range(1, len(canciones)):
        actual = canciones[i]
        j = i - 1
        while j >= 0 and canciones[j].duracion_seg > actual.duracion_seg:
            canciones[j + 1] = canciones[j]
            j -= 1
        canciones[j + 1] = actual
    return canciones

"""TEORIA: En Insercion conserva el orden relativo de claves iguales ; en seleccion no lo garantiza."""