class CancionNoEncontradaError(Exception):
    pass

class Biblioteca:
    def __init__(self):
        self._canciones = {}

    def agregar (self, cancion: Cancion):
        self._canciones[cancion.id] = cancion

    def cantidad(self) -> int:
        return len(self._canciones)

    def obtener(self, id: int) -> Cancion:
        if id not in self._canciones:
            raise CancionNoEncontradaError(f"La cancion con ID {id} no fue encontrada.")
        return self._canciones[id]

    def listar(self) -> list:
        return [str(cancion) for cancion in self._canciones.values()]

    def __iter__(self):
        return iter(self._canciones.values())

# RTA teoria: La biblioteca almacena el catalogo completo y centralizado de todas las instancias unicas de canciones 
# disponibles en el sistema; mientras que una playlist guarda unicamente referencias u ordenamientos especificos de 
#canciones para su reproduccion, sin duplicar los datos ni la informacion general de las mismas.