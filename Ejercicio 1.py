class Cancion:
    def init(self, id, titulo, artista, album, genero, anio, duracion_seg):
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

    def str(self):
        return (f"#{self.id} {self.titulo} | {self.artista} | "
                f"{self.anio} | {self.duracion_mmss()}")

    def eq(self, otro):
        if not isinstance(otro, Cancion):
            return NotImplemented
        return self.id == otro.id

    def hash(self):
        # Si se define eq, hay que definir hash para que siga siendo hasheable.
        return hash(self.id)
# TEORIA
# La duracion se guarda en segundos enteros porque es un dato numerico con el que
# se puede operar (sumar duraciones de una playlist, ordenar, comparar) sin tener
# que parsear texto. El formato "m:ss" es solo una forma de mostrarla, por eso
# duracion_mmss la calcula cuando hace falta
