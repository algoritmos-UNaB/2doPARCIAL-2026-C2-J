from ejercicio_01 import Pokemon


def _valor_orden(pokemon: Pokemon, campo: str) -> int:
    if campo == "ataque":
        return pokemon.ataque
    if campo == "velocidad":
        return pokemon.velocidad
    if campo == "nro":
        return pokemon.id
    raise ValueError(f"Campo no soportado para ordenamiento: {campo}")


def _debe_ir_antes(valor_a: int, valor_b: int, descendente: bool) -> bool:
    if descendente:
        return valor_a > valor_b
    return valor_a < valor_b


def ordenar_seleccion(
    pokemones: list[Pokemon],
    campo: str,
    descendente: bool = False,
) -> list[Pokemon]:
    n = len(pokemones)
    for i in range(n):
        idx_extremo = i
        clave_extremo = _valor_orden(pokemones[idx_extremo], campo)

        for j in range(i + 1, n):
            clave_actual = _valor_orden(pokemones[j], campo)
            if _debe_ir_antes(clave_actual, clave_extremo, descendente):
                idx_extremo = j
                clave_extremo = clave_actual

        if idx_extremo != i:
            pokemones[i], pokemones[idx_extremo] = pokemones[idx_extremo], pokemones[i]

    return pokemones


def ordenar_insercion(
    pokemones: list[Pokemon],
    campo: str,
    descendente: bool = False,
) -> list[Pokemon]:
    for i in range(1, len(pokemones)):
        actual = pokemones[i]
        clave_actual = _valor_orden(actual, campo)
        j = i - 1

        while j >= 0 and _debe_ir_antes(clave_actual, _valor_orden(pokemones[j], campo), descendente):
            pokemones[j + 1] = pokemones[j]
            j -= 1

        pokemones[j + 1] = actual

    return pokemones


# TEORIA: El ordenamiento por insercion es estable, y un algoritmo de ordenamiento es estable cuando preserva el orden relativo original de los elementos que tienen la misma clave