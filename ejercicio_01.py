class Cancion:
    def __init__(self, id: int, titulo: str, artista: str, album: str, genero: str, anio: int, duracion_seg: int):
        self.id = int(id)
        self.titulo = str(titulo)
        self.artista = str(artista)
        self.album = str(album)
        self.genero = str(genero)
        self.anio = int(anio)
        self.duracion_seg = int(duracion_seg)

    def duracion_mmss(self):
        minutos = self.duracion_seg // 60
        segundos = self.duracion_seg % 60
        return f"{minutos}:{segundos:02d}"
    
    def __str__(self):
        return f'#{self.id} {self.titulo} | {self.artista} | {self.anio} | {self.duracion_mmss()}'
    
    def __eq__(self, otro):
        if isinstance(otro, Cancion):
            return self.id == otro.id
        return False


"""
Respuesta: Guardar la duracion como un int permite realizar operaciones numericas como sumar el total de una playlist o comparar canciones. Si la guardaramos como string tendriamos que cortar el texto y convertirlo a int para poder comparar.
"""