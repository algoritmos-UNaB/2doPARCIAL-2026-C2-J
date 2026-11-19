import csv
import os

ENCABEZADO_ESPERADO = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]

def guardar_canciones_csv(ruta: str, biblioteca: Biblioteca):
    with open(ruta, mode="w", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(ENCABEZADO_ESPERADO)
        for c in biblioteca:
            escritor.writerow([c.id, c.titulo, c.artista, c.album, c.genero, c.anio, c.duracion_seg])

def cargar_canciones_csv(ruta: str) -> Biblioteca:
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"El archivo '{ruta}' no existe.")
    biblioteca = Biblioteca()
    with open(ruta, mode="r", encoding="utf-8") as f:
        lector = csv.reader(f)
        try:
            encabezado = next(lector)
        except StopIteration:
            raise ArchivoInvalidoError("El archivo CSV esta vacio.")

        if encabezado != ENCABEZADO_ESPERADO:
            raise ArchivoInvalidoError("El encabezado del CSV no coincide con el formato requerido.")
        for num_linea, fila in enumerate(lector, start=2):
            if len(fila) < 7:
                raise ArchivoInvalidoError(f"Fila {num_linea} tiene menos de 7 columnas.")
            try:
                c = Cancion(
                    id=int(fila),
                    titulo=fila[6],
                    artista=fila[7],
                    album=fila[8],
                    genero=fila[9],
                    anio=int(fila[10]),
                    duracion_seg=int(fila[11])
                )
                biblioteca.agregar(c)
            except ValueError:
                raise ArchivoInvalidoError(f"Error de formato de datos en la fila {num_linea}.")
    return biblioteca

# Rta: Si, es necesario leer secuencialmente las 49 filas anteriores porque las lineas en un archivo 
#CSV tienen una longitud en bytes variable al estar delimitadas por saltos de linea, impidiendo calcular el offset 
#exacto en disco sin procesar el texto previo.