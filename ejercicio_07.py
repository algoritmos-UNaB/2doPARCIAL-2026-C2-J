def busqueda_lineal(recetas, ingredientes, campo, valor) :
    if campo not in ("nombre", "categoria", "ingrediente"):
        raise ValueError(f"Campo de busqueda invalido: {campo}")

    coincidencias = []
    for Receta in recetas:
        if campo == "nombre" :
            coincide = receta.nombre == valor
        elif campo == "categoria":
            coincide = receta.categoria == valor
        else:
            coincide = any(receta_id == receta.id and nombre == valor
                for receta_id, nombre, _cantidad, _unidad in ingredientes )
            
        if coincide :
            coincidencias.append(receta)

    return coincidencias


def busqueda_binaria(recetas, campo, valor):
    
    inicio = 0
    fin = len(recetas) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        receta = recetas[medio]

        if receta.nombre == valor:
            return receta
        if receta.nombre < valor:
            inicio = medio + 1
        else:
            fin = medio - 1

    return None 

# TEORIA : no, no es confiable. Solo es confiable si la lista esta ordenada del msimo modo que se compara      