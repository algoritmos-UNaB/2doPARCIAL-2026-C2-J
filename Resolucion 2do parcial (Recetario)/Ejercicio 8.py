ORDEN_DIFICULTAD = {"baja": 0, "media": 1, "alta": 2}


def _clave(receta, campo):
    """Valor por el que se compara la receta según el campo."""
    if campo == "tiempo":
        return receta.tiempo_min
    if campo == "dificultad":
        return ORDEN_DIFICULTAD[receta.dificultad]
    raise ValueError(f"Campo de ordenamiento inválido: {campo}")


def ordenar_seleccion(recetas, campo, descendente=False):
    """Ordena `recetas` in situ por selección y devuelve esa misma lista."""
    n = len(recetas)
    for i in range(n - 1):
        elegido = i
        for j in range(i + 1, n):
            clave_j = _clave(recetas[j], campo)
            clave_elegido = _clave(recetas[elegido], campo)
            if descendente:
                if clave_j > clave_elegido:
                    elegido = j
            else:
                if clave_j < clave_elegido:
                    elegido = j
        if elegido != i:
            recetas[i], recetas[elegido] = recetas[elegido], recetas[i]
    return recetas


def ordenar_insercion(recetas, campo, descendente=False):
    """Ordena `recetas` in situ por inserción y devuelve esa misma lista."""
    for i in range(1, len(recetas)):
        actual = recetas[i]
        clave_actual = _clave(actual, campo)
        j = i - 1
        while j >= 0:
            clave_j = _clave(recetas[j], campo)
            if descendente:
                debe_correr = clave_j < clave_actual
            else:
                debe_correr = clave_j > clave_actual
            if not debe_correr:
                break
            recetas[j + 1] = recetas[j]
            j -= 1
        recetas[j + 1] = actual
    return recetas


# TEORIA
# El estable es el ordenamiento por inserción; estable significa que dos
# elementos con la misma clave conservan entre sí el orden relativo que tenían
# antes de ordenar (la selección, al intercambiar a distancia, puede alterarlo).