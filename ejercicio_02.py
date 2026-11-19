class PokemonNoEncontrado(Exception):
    pass


class Pokedex:
    def __init__(self):
        self._pokemones = []

    def agregar(self, pokemon):
        for i, actual in enumerate(self._pokemones):
            if actual.id == pokemon.id:
                self._pokemones[i] = pokemon
                return
        self._pokemones.append(pokemon)

    def obtener(self, id):
        for pokemon in self._pokemones:
            if pokemon.id == id:
                return pokemon
        raise PokemonNoEncontrado(f"No se encontró el Pokémon con id {id}")

    def listar(self):
        return list(self._pokemones)

    def cantidad(self):
        return len(self._pokemones)


# TEORIA: Quien llama gana un error inmediato y explícito en vez de un None silencioso que fallaría más adelante, lejos de donde está el problema real, y puede decidir qué hacer con un try/except.
