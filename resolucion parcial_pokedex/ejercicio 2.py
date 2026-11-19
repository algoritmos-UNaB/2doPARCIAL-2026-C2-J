from ejercicio_01 import Pokemon


class PokemonNoEncontrado(Exception):
    pass


class Pokedex:
    def __init__(self) -> None:
        self._pokemones: list[Pokemon] = []

    def agregar(self, pokemon: Pokemon) -> None:
        for i, existente in enumerate(self._pokemones):
            if existente == pokemon:
                self._pokemones[i] = pokemon
                return
        self._pokemones.append(pokemon)

    def obtener(self, id: int) -> Pokemon:
        for pokemon in self._pokemones:
            if pokemon.id == id:
                return pokemon
        raise PokemonNoEncontrado(f"No se encontro ningun Pokemon con id {id}.")

    def listar(self) -> list[Pokemon]:
        return list(self._pokemones)

    def cantidad(self) -> int:
        return len(self._pokemones)


# TEORIA: Quien llama al metodo gana separar el flujo normal de la condicion de error y evitar errores silenciosos por un None inesperado, pudiendo capturar PokemonNoEncontrado de forma explicita.