""" Ejercicio 9 — `canciones.csv` (9 pts)

Persistir la biblioteca en CSV, UTF-8, separador coma, con encabezado:

```text
id,titulo,artista,album,genero,anio,duracion_seg
```

```python
def guardar_canciones_csv(ruta, biblioteca): ...
def cargar_canciones_csv(ruta) -> Biblioteca: ...
```

`cargar_canciones_csv` rearma objetos `Cancion`. Lanza `ArchivoInvalidoError` si el archivo no existe, si el encabezado no es el pedido o si una fila tiene menos columnas.

Las versiones quedan fuera de este archivo.

**Teoría.** Para leer la canción de la fila 50, ¿hay que recorrer las filas anteriores? Explicar en una oración por qué, a partir de cómo está guardado el CSV.
"""
import csv
from pathlib import Path

ENCABEZADO_ESPERADO = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]


class ArchivoInvalidoError(Exception):
    def __init__(self, mensaje: str = "El archivo CSV no es valido."):
        super().__init__(mensaje)


def _obtener_canciones_biblioteca(biblioteca) -> list:
    if hasattr(biblioteca, "canciones"):
        return list(biblioteca.canciones)
    if hasattr(biblioteca, "_canciones"):
        return list(biblioteca._canciones)
    raise AttributeError("La clase Biblioteca tiene `canciones` o `_canciones`.")

def guardar_canciones_csv(ruta, biblioteca) -> None:
    canciones = _obtener_canciones_biblioteca(biblioteca)
    ruta_path = Path(ruta)

    with ruta_path.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerow(ENCABEZADO_ESPERADO)
        for c in canciones:
            escritor.writerow([
                c.id,
                c.titulo,
                c.artista,
                c.album,
                c.genero,
                c.anio,
                c.duracion_seg,
            ])


def cargar_canciones_csv(ruta) -> "Biblioteca":
    ruta_path = Path(ruta)
    if not ruta_path.is_file():
        raise ArchivoInvalidoError(f"El archivo no existe: {ruta_path}")

    with ruta_path.open("r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo, delimiter=",")
        encabezado = next(lector, None)
        if encabezado != ENCABEZADO_ESPERADO:
            raise ArchivoInvalidoError(
                f"Encabezado invalido: se esperaba {ENCABEZADO_ESPERADO}, se obtuvo {encabezado}."
            )

        canciones = []
        for num_fila, fila in enumerate(lector, start=2):
            if len(fila) < len(ENCABEZADO_ESPERADO):
                raise ArchivoInvalidoError(
                    f"La fila {num_fila} tiene menos columnas ({len(fila)}) que las esperadas ({len(ENCABEZADO_ESPERADO)})."
                )

            cancion = Cancion(
                id=int(fila[0]),
                titulo=fila[1],
                artista=fila[2],
                album=fila[3],
                genero=fila[4],
                anio=int(fila[5]),
                duracion_seg=int(fila[6]),
            )
            canciones.append(cancion)

    return Biblioteca(canciones)

"""
TEORIA: Si, porque en un CSV cada registro es una linea de texto de longitud variable separada
 por saltos de linea, por lo que no se sabe donde empieza la fila 50 sin leer las anteriores."""