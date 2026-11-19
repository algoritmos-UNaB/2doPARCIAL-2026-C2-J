def busqueda_lineal(recetas, ingredientes, campo, valor):
    resultado = []
    for receta in recetas:
        if campo == "nombre":
            coincide = receta.nombre == valor
        elif campo == "categoria":
            coincide = receta.categoria == valor
        elif campo == "ingrediente":
            coincide = False
            for fila in ingredientes:
                if fila[0] == receta.id and fila[1] == valor:
                    coincide = True
                    break
        else:
            coincide = False
        if coincide:
            resultado.append(receta)
    return resultado


def busqueda_binaria(recetas, campo, valor):
    if campo != "nombre":
        return None
    inicio = 0
    fin = len(recetas) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        nombre = recetas[medio].nombre
        if nombre == valor:
            return recetas[medio]
        if nombre < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None


# TEORIA
#  No, porque la búsqueda binaria necesita que la lista esté ordenada
# por el mismo campo por el que busca para poder descartar mitades correctamente.