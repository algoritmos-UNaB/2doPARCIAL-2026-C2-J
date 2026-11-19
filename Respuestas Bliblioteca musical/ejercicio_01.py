class Cancion:
    def __init__(self, id: int, titulo: str, artista: str, album: str, genero: str, anio: int, duracion_seg: int):
        self.id = int(id)
        self.titulo = str(titulo)
        self.artista = str(artista)
        self.album = str(album)
        self.genero = str(genero)
        self.anio = int(anio)
        self.duracion_seg = int(duracion_seg)

    def duracion_mmss(self) -> str:
        minutos = self.duracion_seg // 60
        segundos = self.duracion_seg % 60
        return f"{minutos}:{segundos:02d}"

    def __str__(self) -> str:
        return f"#{self.id} {self.titulo} | {self.artista} | {self.anio} | {self.duracion_mmss()}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Cancion):
            return False
        return self.id == other.id

# Rta teoria: Guardar la duracion en segundos enteros facilita realizar operaciones aritmeticas directas
#(como calcular la duracion total de una playlist o hacer comparaciones cuantitativas para ordenamiento) de 
#forma eficiente Ademas, evita la necesidad de parsear cadenas de texto constantemente cada vez que se debe manipular o 
#comparar el tiempo de ejecucion.