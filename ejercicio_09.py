import csv
from pathlib import Path

from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca


class ArchivoInvalidoError(Exception):
    pass


ENCABEZADO_ESPERADO = [
    "id",
    "titulo",
    "artista",
    "album",
    "genero",
    "anio",
    "duracion_seg",
]


def guardar_canciones_csv(ruta, biblioteca: Biblioteca) -> None:
    ruta_path = Path(ruta)
    with ruta_path.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerow(ENCABEZADO_ESPERADO)
        for cancion in biblioteca:
            escritor.writerow(
                [
                    cancion.id,
                    cancion.titulo,
                    cancion.artista,
                    cancion.album,
                    cancion.genero,
                    cancion.anio,
                    cancion.duracion_seg,
                ]
            )


def cargar_canciones_csv(ruta) -> Biblioteca:
    ruta_path = Path(ruta)
    if not ruta_path.is_file():
        raise ArchivoInvalidoError(f"El archivo no existe: {ruta}")

    biblioteca = Biblioteca()
    try:
        with ruta_path.open("r", encoding="utf-8", newline="") as archivo:
            lector = csv.reader(archivo, delimiter=",")
            encabezado = next(lector, None)
            if encabezado != ENCABEZADO_ESPERADO:
                raise ArchivoInvalidoError(
                    f"Encabezado inválido: se esperaba {ENCABEZADO_ESPERADO}, se obtuvo {encabezado}."
                )

            for fila in lector:
                if len(fila) < len(ENCABEZADO_ESPERADO):
                    raise ArchivoInvalidoError(
                        f"Fila con menos columnas de las esperadas: {fila}"
                    )

                try:
                    cancion = Cancion(
                        id=int(fila[0]),
                        titulo=fila[1],
                        artista=fila[2],
                        album=fila[3],
                        genero=fila[4],
                        anio=int(fila[5]),
                        duracion_seg=int(fila[6]),
                    )
                except ValueError as exc:
                    raise ArchivoInvalidoError(f"Datos inválidos en fila {fila}: {exc}") from exc

                biblioteca.agregar(cancion)
    except OSError as exc:
        raise ArchivoInvalidoError(f"Error al leer el archivo CSV: {exc}") from exc

    return biblioteca


# Teoría:
# Sí, hay que recorrer las filas anteriores porque en un archivo CSV de texto
# separado por comas las líneas tienen longitud variable y no están indexadas
# por posición de bytes, por lo que para llegar a la fila 50 hay que avanzar
# secuencialmente desde el inicio pasando por los saltos de línea previos.