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
        minutos = self.duracion_seg // 60
        segundos = self.duracion_seg % 60
        return f"{minutos}:{segundos:02d}"

    def __str__(self):
        return (f"#{self.id} {self.titulo} | {self.artista} | "
                f"{self.anio} | {self.duracion_mmss()}")

    def __eq__(self, otra):
        if not isinstance(otra, Cancion):
            return False
        return self.id == otra.id


if __name__ == "__main__":
    c = Cancion(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota",
                "Un baión para el ojo idiota", "Rock", 1988, 316)
    print(c)                    # #12 Jijiji | Patricio Rey ... | 1988 | 5:16
    print(Cancion(1, "a", "b", "c", "d", 2000, 65).duracion_mmss())  # 1:05
    print(Cancion(2, "a", "b", "c", "d", 2000, 59).duracion_mmss())  # 0:59

# TEORÍA:
# Guardar la duración en segundos enteros permite operar directamente con ella
# (sumar duraciones de una playlist, comparar u ordenar canciones) sin tener que
# parsear un texto. El formato "m:ss" es solo una forma de mostrarla, y se
# calcula cuando hace falta, evitando inconsistencias o errores de formato.