from ejercicio_02 import Pokedex, PokemonNoEncontrado


def descendientes(
    origen_id: int,
    pokedex: Pokedex,
    aristas: list[tuple[int, int]],
) -> list[int]:
    pokedex.obtener(origen_id)

    for _, destino_id in aristas:
        pokedex.obtener(destino_id)

    return _descendientes_rec(origen_id, aristas)


def _descendientes_rec(actual_id: int, aristas: list[tuple[int, int]]) -> list[int]:
    destinos = [destino_id for orig_id, destino_id in aristas if orig_id == actual_id]
    if not destinos:
        return []

    resultado: list[int] = []
    for destino_id in destinos:
        resultado.append(destino_id)
        resultado.extend(_descendientes_rec(destino_id, aristas))
    return resultado

    #teoria:Traza de llamadas para descendientes(4) con aristas (4, 5) y (5, 6): 1) descendientes(4) -> 2) descendientes(5) -> 3) descendientes(6) [caso base: sin destinos, retorna []].