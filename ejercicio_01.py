"""Ejercicio 1 - Cancion."""

class Cancion:
    def __init__(self, id, titulo, artista, album, genero, anio, duracion_seg):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = anio
        self.duracion_seg = duracion_seg

    def duracion_mmss(self):
        minutos, segundos = divmod(self.duracion_seg, 60)
        return f"{minutos}:{segundos:02d}"

    def __str__(self):
        return (f"#{self.id} {self.titulo} | {self.artista} | "
                f"{self.anio} | {self.duracion_mmss()}")

    def __eq__(self, otro):
        return self.id == otro.id

# TEORIA
# Guardar la duracion en segundos enteros permite sumar, comparar y ordenar
# con aritmetica simple (por ejemplo duracion_total de una playlist o ordenar
# por duracion), cosa que con un string "5:16" obligaria a decodificar cada vez.
# Ademas hay una unica representacion de cada duracion, y el formato m:ss es
# solo una presentacion que se calcula a pedido.