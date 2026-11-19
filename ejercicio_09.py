import csv

from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca


class ArchivoInvalidoError(Exception):
    pass


ENCABEZADO = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]


def guardar_canciones_csv(ruta, biblioteca):
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerow(ENCABEZADO)
        for c in biblioteca:
            escritor.writerow([c.id, c.titulo, c.artista, c.album,
                               c.genero, c.anio, c.duracion_seg])


def cargar_canciones_csv(ruta) -> Biblioteca:
    try:
        archivo = open(ruta, "r", encoding="utf-8", newline="")
    except FileNotFoundError:
        raise ArchivoInvalidoError(f"El archivo {ruta} no existe")

    with archivo:
        lector = csv.reader(archivo, delimiter=",")
        encabezado = next(lector, None)
        if encabezado != ENCABEZADO:
            raise ArchivoInvalidoError("El encabezado no es el pedido")

        biblioteca = Biblioteca()
        for numero, fila in enumerate(lector, start=2):
            if len(fila) < len(ENCABEZADO):
                raise ArchivoInvalidoError(f"La fila {numero} tiene menos columnas")
            try:
                cancion = Cancion(int(fila[0]), fila[1], fila[2], fila[3],
                                  fila[4], int(fila[5]), int(fila[6]))
            except ValueError:
                raise ArchivoInvalidoError(f"La fila {numero} tiene datos inválidos")
            biblioteca.agregar(cancion)
        return biblioteca


if __name__ == "__main__":
    b = Biblioteca()
    b.agregar(Cancion(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota",
                      "Un baión para el ojo idiota", "Rock", 1988, 316))
    b.agregar(Cancion(30, "De Música Ligera", "Soda Stereo", "Canción animal", "Rock", 1990, 213))
    b.agregar(Cancion(20, "Alfonsina y el mar", "Mercedes Sosa", "Mujeres argentinas", "Folklore", 1969, 297))

    guardar_canciones_csv("canciones.csv", b)
    print("Guardado.")

    cargada = cargar_canciones_csv("canciones.csv")
    print("Cargadas:", cargada.cantidad())
    for linea in cargada.listar():
        print(" ", linea)

    try:
        cargar_canciones_csv("no_existe.csv")
    except ArchivoInvalidoError as e:
        print("Error:", e)

# TEORÍA:
# Sí, hay que recorrer las filas anteriores: el CSV es un archivo de texto donde
# cada fila tiene largo variable y termina en un salto de línea, así que no hay
# forma de saber en qué posición empieza la fila 50 sin leer las 49 anteriores.