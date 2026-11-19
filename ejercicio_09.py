# ejercicio_09.py
import csv
from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca

ENCABEZADO = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]


class ArchivoInvalidoError(Exception):
    """Se lanza cuando el archivo no existe o su contenido no es el esperado."""
    pass


def guardar_canciones_csv(ruta, biblioteca):
    with open(ruta, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(ENCABEZADO)
        for c in biblioteca:
            writer.writerow([c.id, c.titulo, c.artista, c.album,
                             c.genero, c.anio, c.duracion_seg])


def cargar_canciones_csv(ruta) -> Biblioteca:
    try:
        f = open(ruta, mode="r", newline="", encoding="utf-8")
    except FileNotFoundError:
        raise ArchivoInvalidoError(f"El archivo {ruta!r} no existe.")

    with f:
        reader = csv.reader(f)

        try:
            encabezado = next(reader)
        except StopIteration:
            raise ArchivoInvalidoError("El archivo está vacío: falta el encabezado.")
        if encabezado != ENCABEZADO:
            raise ArchivoInvalidoError(
                f"Encabezado inválido: se esperaba {','.join(ENCABEZADO)}."
            )

        biblioteca = Biblioteca()
        for nro, fila in enumerate(reader, start=2):   # la fila 1 es el encabezado
            if not fila:                               # línea en blanco: se ignora
                continue
            if len(fila) < len(ENCABEZADO):
                raise ArchivoInvalidoError(
                    f"Fila {nro} incompleta: tiene {len(fila)} columnas "
                    f"y se esperaban {len(ENCABEZADO)}."
                )
            try:
                biblioteca.agregar(Cancion(*fila[:len(ENCABEZADO)]))
            except ValueError:
                raise ArchivoInvalidoError(
                    f"Fila {nro} inválida: id, anio y duracion_seg deben ser números."
                )
        return biblioteca

"""Sii, hay que recorrer las filas anteriores, porque un CSV es un archivo de texto cuyas filas tienen largo variable y estan 
separadas solo por saltos de linea, asi que no se puede calcular en que byte empieza la fila 50 sin leer antes las 49 anteriores 
para ir contando esos saltos."""

