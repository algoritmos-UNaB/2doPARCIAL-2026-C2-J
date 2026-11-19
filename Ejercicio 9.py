import csv
import os

from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca

ENCABEZADO = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]

class ArchivoInvalidoError(Exception):
    """El archivo no existe o su formato no es el esperado."""

    def __init__(self, mensaje="El archivo es invalido"):
        super().__init__(mensaje)


def guardar_canciones_csv(ruta, biblioteca):
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo, lineterminator="\n")
        escritor.writerow(ENCABEZADO)
        for c in biblioteca:
            escritor.writerow([c.id, c.titulo, c.artista, c.album,
                               c.genero, c.anio, c.duracion_seg])

def cargar_canciones_csv(ruta):
    if not os.path.isfile(ruta):
        raise ArchivoInvalidoError(f"El archivo {ruta!r} no existe")

    biblioteca = Biblioteca()
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo)
        encabezado = next(lector, None)
        if encabezado != ENCABEZADO:
            raise ArchivoInvalidoError(
                f"Encabezado invalido: se esperaba {','.join(ENCABEZADO)}")
        for numero, fila in enumerate(lector, start=2):
            if not fila:
                continue  # linea en blanco
            if len(fila) < len(ENCABEZADO):
                raise ArchivoInvalidoError(
                    f"La fila {numero} tiene {len(fila)} columnas y se esperaban {len(ENCABEZADO)}")
            try:
                cancion = Cancion(int(fila[0]), fila[1], fila[2], fila[3],
                                  fila[4], int(fila[5]), int(fila[6]))
            except ValueError:
                raise ArchivoInvalidoError(
                    f"La fila {numero} tiene un valor numerico invalido")
            biblioteca.agregar(cancion)
    return biblioteca

# TEORIA
# Si, hay que recorrer las filas anteriores. El CSV es texto y cada fila tiene
# una longitud variable (los titulos y artistas miden distinto), asi que no se
# puede calcular en que byte empieza la fila 50: hay que leer y contar los
# saltos de linea de las 49 anteriores.
