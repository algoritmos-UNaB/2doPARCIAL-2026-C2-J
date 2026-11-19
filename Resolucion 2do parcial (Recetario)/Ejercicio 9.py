import csv
from ejercicio_01 import Receta
from ejercicio_02 import LibroRecetas


class ArchivoInvalidoError(Exception):
    pass


def guardar_recetas_csv(ruta, libro):
    with open(ruta, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(["id", "nombre", "tiempo_min", "dificultad", "categoria"])
        for r in libro.listar():
            writer.writerow([r.id, r.nombre, r.tiempo_min, r.dificultad, r.categoria])


def cargar_recetas_csv(ruta):
    libro = LibroRecetas()
    with open(ruta, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        try:
            encabezado = next(reader)
        except StopIteration:
            raise ArchivoInvalidoError("Archivo vacío o sin encabezado.")
        if encabezado != ["id", "nombre", "tiempo_min", "dificultad", "categoria"]:
            raise ArchivoInvalidoError("Encabezado inválido.")
        for fila in reader:
            if len(fila) != 5:
                raise ArchivoInvalidoError("Cantidad de columnas inválida.")
            try:
                receta_id = int(fila[0])
                tiempo_min = int(fila[2])
            except ValueError:
                raise ArchivoInvalidoError("Error al convertir valores numéricos.")
            libro.agregar(Receta(receta_id, fila[1], tiempo_min, fila[3], fila[4]))
    return libro


def guardar_ingredientes_csv(ruta, ingredientes):
    with open(ruta, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(["receta_id", "nombre", "cantidad", "unidad"])
        for receta_id, nombre, cantidad, unidad in ingredientes:
            writer.writerow([receta_id, nombre, cantidad, unidad])


def cargar_ingredientes_csv(ruta):
    ingredientes = []
    with open(ruta, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        try:
            encabezado = next(reader)
        except StopIteration:
            raise ArchivoInvalidoError("Archivo vacío o sin encabezado.")
        if encabezado != ["receta_id", "nombre", "cantidad", "unidad"]:
            raise ArchivoInvalidoError("Encabezado inválido.")
        for fila in reader:
            if len(fila) != 4:
                raise ArchivoInvalidoError("Cantidad de columnas inválida.")
            try:
                receta_id = int(fila[0])
                cantidad = int(fila[2]) if fila[2].isdigit() or (fila[2].startswith("-") and fila[2][1:].isdigit()) else float(fila[2])
            except ValueError:
                raise ArchivoInvalidoError("Error al convertir valores numéricos.")
            ingredientes.append((receta_id, fila[1], cantidad, fila[3]))
    return ingredientes


# TEORIA: Sí, hace falta leer los registros anteriores porque los archivos de texto tienen registros de longitud variable y el acceso es secuencial.