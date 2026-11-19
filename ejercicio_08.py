orden_dificultad = {"baja":1, "media" :2, "alta" :3}

def _clave_orden(receta, campo):
    if campo == "tiempo" :
        return receta.tiempo_min
    elif campo == "dificultad":
        return orden_dificultad[receta.dificultad]
    raise ValueError(f"Campo de ordenamiento no soportado: {campo}")


def _debe_ir_antes(a, b, campo, descendente) :
    va = _clave_orden(a, campo)
    vb = _clave_orden(b, campo)
    if descendente:
        return va > vb
    return va < vb

def ordenar_seleccion(recetas, campo, descendente= False) :
    n = len(recetas)
    for i in range(n - 1):
        idx_extremo = i
        for j in range(i + 1, n):
            if _debe_ir_antes(recetas[j], recetas[idx_extremo], campo, descendente):
                idx_extremo = j

        if idx_extremo != i:
            recetas[i], recetas[idx_extremo] = recetas[idx_extremo], recetas[i]
    return recetas


def ordenar_insercion(recetas, campo, descendente=False):
    for i in range(1, len(recetas)):
        actual = recetas[i]
        j = i - 1
        while j >= 0 and _debe_ir_antes(actual, recetas[j], campo, descendente):
            recetas[j + 1] = recetas[j]
            j -= 1

        recetas[j + 1] = actual
    return recetas    

# TEORIA : El algoritmo estable es el de ordenar_insercion, poruqe mantiene el orden originial de los elementos con claves iguales   