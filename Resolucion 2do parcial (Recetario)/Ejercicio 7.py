def busqueda_lineal(recetas, ingredientes, campo, valor):
    coincidencias = []
    for receta in recetas:
        if campo == "nombre":
            if receta.nombre == valor:
                coincidencias.append(receta)
        elif campo == "categoria":
            if receta.categoria == valor:
                coincidencias.append(receta)
        elif campo == "ingrediente":
            for r_id, nombre_ing, _, _ in ingredientes:
                if r_id == receta.id and nombre_ing == valor:
                    coincidencias.append(receta)
                    break
    return coincidencias


def busqueda_binaria(recetas, campo, valor):
    if campo != "nombre":
        return None
    izq = 0
    der = len(recetas) - 1
    while izq <= der:
        medio = (izq + der) // 2
        actual = recetas[medio]
        if actual.nombre == valor:
            return actual
        elif actual.nombre < valor:
            izq = medio + 1
        else:
            der = medio - 1
    return None


# TEORIA: No, porque la búsqueda binaria asume que los elementos están ordenados según el criterio de búsqueda para descartar mitades de forma segura, y al estar ordenada por tiempo el orden alfabético por nombre es arbitrario y puede descartar la mitad que contiene el elemento buscado.