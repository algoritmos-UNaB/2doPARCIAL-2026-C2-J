from ejercicio_01 import Pokemon


def _obtener_clave_busqueda(pokemon: Pokemon, campo: str):
    if campo == "nombre":
        return pokemon.nombre
    if campo == "nro":
        return pokemon.id
    raise ValueError(f"Campo no soportado: {campo}")


def busqueda_lineal(pokemones: list[Pokemon], campo: str, valor: object) -> list[Pokemon]:
    coincidencias: list[Pokemon] = []

    for pokemon in pokemones:
        if campo == "nombre" and pokemon.nombre == valor:
            coincidencias.append(pokemon)
        elif campo == "tipo" and (pokemon.tipo1 == valor or pokemon.tipo2 == valor):
            coincidencias.append(pokemon)
        elif campo == "nro" and pokemon.id == valor:
            coincidencias.append(pokemon)

    return coincidencias


def busqueda_binaria(pokemones: list[Pokemon], campo: str, valor: object) -> Pokemon | None:
    if campo not in ("nombre", "nro"):
        raise ValueError(f"Campo no valido para busqueda binaria: {campo}")

    izquierda = 0
    derecha = len(pokemones) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = pokemones[medio]
        clave_actual = _obtener_clave_busqueda(actual, campo)

        if clave_actual == valor:
            return actual
        if clave_actual < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None


# TEORIA: No, el resultado no es confiable porque la busqueda binaria depende de que la lista este ordenada segun el mismo criterio por el que se busca para descartar correctamente cada mitad.