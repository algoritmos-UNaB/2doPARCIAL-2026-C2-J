from ejercicio_01 import Cancion

class CancionNoEncontradaError(Exception):
    pass


class Biblioteca:
    def __init__(self):
        self.canciones = []
    def agregar(self, cancion):
        self.cancion.append(cancion)
    def cantidad(self):
        return len(self.canciones)
    def obtener(self, id_cancion):
        for cancion in self.canciones:
            if cancion.id == id_cancion:
                return cancion
        raise CancionNoEncontradaError(f'No existe cancion con id {id_cancion}')
    def listar(self):
        resultado = []
        for cancion in self.canciones:
            resultado.append(str(cancion))
        return resultado
    def __iter__(self):
        for cancion in self.canciones:
            yield cancion


"""
La biblioteca guarda el catalogo de todas las canciones disponibles en el sistema. La playlist guarda una lista especifica de canciones seleccionadas por el usuario para ser reproducidas en un orden determinado.
"""