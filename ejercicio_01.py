## Ejercicio 1 — Canción (8 pts)
"""
Definir la clase `Cancion`.

Atributos: `id` (int), `titulo` (str), `artista` (str), `album` (str), 
`genero` (str), `anio` (int), `duracion_seg` (int).

Métodos:

- `duracion_mmss()` 
devuelve la duración como `m:ss`. `316` → `"5:16"`, `65` → `"1:05"`, `59` → `"0:59"`.
- `__str__` devuelve `#12 Jijiji | Patricio Rey y sus Redonditos de Ricota | 1988 | 5:16`.
- `__eq__` compara por `id`.

**Teoría.** La duración se guarda en segundos enteros y `duracion_mmss` la calcula. 
Explicar en dos oraciones por qué conviene guardarla así y no en un string `"5:16"`. dos oraciones por qué conviene guardarla así y no en un string `"5:16"`.
"""
class Cancion:
        def __init__(self, id:int , titulo:str , artista:str , album::str , genero:str, anio:int, duracion_seg:int):
            self.id = id
            self.titulo = titulo
            self.artista = artista
            self.album = album
            self.genero = genero 
            self.anio = anios
            self.duracion_seg = duracion_seg
        
        def duracion_mmss(self):
            min = self.duracion_seg // 60
            seg = self.duracion_seg % 60 
            return f"{min} : {seg: 02d}"
        
        def __str__(self):
            return(
                f"id: {self.id} "
                f"titulo: {self.titulo}"
                f"artista: {self.artista}"
                f"album: {self.album}"
                f"genero: {self.genero}"
                f"anio : {self.anio}"
                f"duracion: {self.duracion_mmss()}"
            )
        def __eq__(self , otra):
            if not isinstance(otra , Cancion):
                return False
            return self.id == otra.id

"""
TEORIA : es necesario que la variable "duracion_seg" este como "int" para que el metodo 
"duracion_mmss()" pueda realizar su calculo y necesariamente; por si en un futuro 
querramos realizar alguna otra operacion como sumar timepos, promedio, etc. 
"""
