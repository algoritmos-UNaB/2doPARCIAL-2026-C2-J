class Cancion:
    def __init__(
        self,
        id: int,
        titulo: str,
        artista: str,
        album: str,
        genero: str,
        anio: int,
        duracion_seg: int,
    ):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = anio
        self.duracion_seg = duracion_seg

    def duracion_mmss(self) -> str:
        minutos = self.duracion_seg // 60
        segundos = self.duracion_seg % 60
        return f"{minutos}:{segundos:02d}"

    def __str__(self) -> str:
        return f"#{self.id} {self.titulo} | {self.artista} | {self.anio} | {self.duracion_mmss()}"

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, Cancion):
            return False
        return self.id == otro.id


# Teoría:
# Guardar la duración en segundos enteros facilita realizar operaciones numéricas
# como sumar duraciones totales, comparar o filtrar canciones por extensión y
# ordenar sin tener que parsear texto cada vez. Además, mantener el formato
# visual en duracion_mmss() evita redundancia y previene inconsistencias al
# modificar o calcular tiempos.