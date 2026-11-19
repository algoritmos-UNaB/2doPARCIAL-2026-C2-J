def _obtener_valor_campo(pokemon, campo):
    if campo == "nombre":
        return pokemon.nombre
    if campo == "nro":
        return pokemon.id
    raise ValueError(f"Campo no soportado: {campo}")


def busqueda_lineal(pokemones, campo, valor):
    coincidencias = []
    for pokemon in pokemones:
        if campo == "nombre" and pokemon.nombre == valor:
            coincidencias.append(pokemon)
        elif campo == "tipo" and (pokemon.tipo1 == valor or pokemon.tipo2 == valor):
            coincidencias.append(pokemon)
        elif campo == "nro" and pokemon.id == valor:
            coincidencias.append(pokemon)
    return coincidencias


def busqueda_binaria(pokemones, campo, valor):
    izquierda = 0
    derecha = len(pokemones) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = _obtener_valor_campo(pokemones[medio], campo)

        if actual == valor:
            return pokemones[medio]
        if actual < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None


# TEORIA: No, porque la búsqueda binaria descarta una mitad asumiendo que la lista está ordenada por el campo buscado, y si está ordenada por ataque esa suposición falla y puede descartar la mitad donde está el nombre, devolviendo None aunque exista.
