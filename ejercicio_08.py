def _clave_orden(pokemon, campo):
    if campo == "ataque":
        return pokemon.ataque
    if campo == "velocidad":
        return pokemon.velocidad
    if campo == "nro":
        return pokemon.id
    raise ValueError(f"Campo no soportado: {campo}")


def _debe_ir_antes(a, b, descendente):
    if descendente:
        return a > b
    return a < b


def ordenar_seleccion(pokemones, campo, descendente=False):
    n = len(pokemones)
    for i in range(n):
        idx_extremo = i
        val_extremo = _clave_orden(pokemones[idx_extremo], campo)
        for j in range(i + 1, n):
            val_actual = _clave_orden(pokemones[j], campo)
            if _debe_ir_antes(val_actual, val_extremo, descendente):
                idx_extremo = j
                val_extremo = val_actual
        if idx_extremo != i:
            pokemones[i], pokemones[idx_extremo] = pokemones[idx_extremo], pokemones[i]
    return pokemones


def ordenar_insercion(pokemones, campo, descendente=False):
    for i in range(1, len(pokemones)):
        actual = pokemones[i]
        val_actual = _clave_orden(actual, campo)
        j = i - 1
        while j >= 0 and _debe_ir_antes(val_actual, _clave_orden(pokemones[j], campo), descendente):
            pokemones[j + 1] = pokemones[j]
            j -= 1
        pokemones[j + 1] = actual
    return pokemones

# TEORIA: Inserción es estable, porque un algoritmo es estable cuando mantiene el orden relativo de los elementos con el mismo valor del campo, y selección no lo es porque sus intercambios a distancia pueden saltear a un elemento igual.
