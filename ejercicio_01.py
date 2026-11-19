class Cancion:
    def __init__(self, id, titulo, artista, album, genero, anio, duracion_seg):
        self.id = int(id)
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = int(anio)
        self.duracion_seg = int(duracion_seg)

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

    def __hash__(self):
        return hash(self.id)

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'artista': self.artista,
            'album': self.album,
            'genero': self.genero,
            'anio': self.anio,
            'duracion_seg': self.duracion_seg,
        }

#Conviene guardar la duración como entero en segundos porque permite hacer operaciones numéricas 
#directamente (sumar la duración de una playlist, ordenar o comparar canciones) sin tener que parsear texto.
#El formato m:ss es solo una representación para mostrar, y calcularlo a partir del entero evita
#inconsistencias y valores inválidos como "5:75".