ORDEN_DIFICULTAD = {"baja": 0, "media": 1, "alta": 2}


def _clave(receta, campo):
    if campo == "tiempo":
        return receta.tiempo_min
    return ORDEN_DIFICULTAD[receta.dificultad]


def _va_antes(a, b, campo, descendente):
    clave_a = _clave(a, campo)
    clave_b = _clave(b, campo)
    if descendente:
        return clave_a > clave_b
    return clave_a < clave_b


def ordenar_seleccion(recetas, campo, descendente=False):
    n = len(recetas)
    for i in range(n - 1):
        elegido = i
        for j in range(i + 1, n):
            if _va_antes(recetas[j], recetas[elegido], campo, descendente):
                elegido = j
        recetas[i], recetas[elegido] = recetas[elegido], recetas[i]
    return recetas


def ordenar_insercion(recetas, campo, descendente=False):
    for i in range(1, len(recetas)):
        actual = recetas[i]
        j = i - 1
        while j >= 0 and _va_antes(actual, recetas[j], campo, descendente):
            recetas[j + 1] = recetas[j]
            j -= 1
        recetas[j + 1] = actual
    return recetas


# TEORIA
# # El ordenamiento por inserción es estable.
# Un algoritmo es estable cuando conserva el orden relativo de los elementos que tienen la misma clave