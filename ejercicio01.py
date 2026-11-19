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
        if not isinstance(otro, Cancion):
            return NotImplemented
        return self.id == otro.id


# Datos de prueba
DATOS_PRUEBA = [
    (1, "De Musica Ligera", "Soda Stereo", "Cancion Animal", "Rock", 1990, 213),
    (12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota", "Un Baion para el Ojo Idiota", "Rock", 1988, 316),
    (13, "Ji Ji Ji", "Patricio Rey y sus Redonditos de Ricota", "En Directo", "Rock", 1992, 318),
    (15, "Alfonsina y el mar", "Mercedes Sosa", "Mujeres Argentinas", "Folklore", 1969, 298),
    (16, "Gracias a la Vida", "Mercedes Sosa", "Hasta la Victoria", "Folklore", 1971, 271),
    (61, "Gracias a la Vida", "Violeta Parra", "Las Ultimas Composiciones", "Folklore", 1966, 258),
    (62, "De Musica Ligera (Unplugged)", "Soda Stereo", "Comfort y Musica Para Volar", "Rock", 1996, 221),
    (70, "Ji Ji Ji (Remix)", "Patricio Rey y sus Redonditos de Ricota", "Remixes", "Rock", 2020, 300),
]

# TEORIA
# Guardar la duracion en segundos enteros permite sumar, comparar y ordenar
# con aritmetica simple (por ejemplo duracion_total de una playlist o ordenar
# por duracion), cosa que con un string "5:16" obligaria a decodificar cada vez.
# Ademas hay una unica representacion de cada duracion, y el formato m:ss es
# solo una presentacion que se calcula a pedido.