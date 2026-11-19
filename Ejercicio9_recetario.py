import csv

from Ejercicio1_recetario import Receta
from Ejercicio2_recetario import LibroRecetas

ENCABEZADO_RECETAS = ["id", "nombre", "tiempo_min", "dificultad", "categoria"]
ENCABEZADO_INGREDIENTES = ["receta_id", "nombre", "cantidad", "unidad"]


class ArchivoInvalidoError(Exception):
    pass


def _numero(texto):
    try:
        return int(texto)
    except ValueError:
        return float(texto)


def _leer_filas(ruta, encabezado):
    try:
        with open(ruta, "r", newline="", encoding="utf-8") as f:
            filas = list(csv.reader(f))
    except (UnicodeError, csv.Error) as error:
        raise ArchivoInvalidoError("Archivo ilegible") from error
    if not filas or filas[0] != encabezado:
        raise ArchivoInvalidoError("Falta el encabezado o es incorrecto")
    datos = filas[1:]
    for fila in datos:
        if len(fila) != len(encabezado):
            raise ArchivoInvalidoError("Fila con cantidad de columnas incorrecta")
    return datos


def guardar_recetas_csv(ruta, libro):
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(ENCABEZADO_RECETAS)
        for r in libro.listar():
            escritor.writerow([r.id, r.nombre, r.tiempo_min, r.dificultad, r.categoria])


def cargar_recetas_csv(ruta):
    libro = LibroRecetas()
    for fila in _leer_filas(ruta, ENCABEZADO_RECETAS):
        try:
            libro.agregar(Receta(int(fila[0]), fila[1], int(fila[2]), fila[3], fila[4]))
        except ValueError:
            raise ArchivoInvalidoError("Número inválido en recetas")
    return libro


def guardar_ingredientes_csv(ruta, ingredientes):
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(ENCABEZADO_INGREDIENTES)
        for fila in ingredientes:
            escritor.writerow(fila)


def cargar_ingredientes_csv(ruta):
    resultado = []
    for fila in _leer_filas(ruta, ENCABEZADO_INGREDIENTES):
        try:
            resultado.append((int(fila[0]), fila[1], _numero(fila[2]), fila[3]))
        except ValueError:
            raise ArchivoInvalidoError("Número inválido en ingredientes")
    return resultado


# TEORIA
# Sí, hace falta leer los anteriores: en un archivo de texto CSV las filas tienen largo variable, así que
# para llegar al registro 10 hay que recorrer los anteriores. El acceso es secuencial.
