import csv
from ejercicio_01 import Receta 
from ejercicio_02 import LibroRecetas

class ArchivoInvalidoError(Exception):
    pass

CABECERA_RECETAS = ["id", "nombre", "tiempo_min", "dificultad", "categoria"]
CABECERA_INGREDIENTES = ["receta_id", "nombre", "cantidad", "unidad"]


def guardar_recetas_csv(ruta, libro) :
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerow(CABECERA_RECETAS)
        for receta in libro.listar():
            escritor.writerow([receta.id, receta.nombre, receta.tiempo_min, receta.dificultad, receta.categoria])
                

def cargar_recetas_csv(ruta):
    libro = LibroRecetas()

    with open(ruta, "r", newline="", encoding="utf-8") as archivo :
        lector = csv.reader(archivo, delimiter=",")
        cabecera = next(lector, None)

        if cabecera != CABECERA_RECETAS:
            raise ArchivoInvalidoError("Encabezado de recetas ausente o invalido")

        for numero_fila, fila in enumerate(lector, start=2):
            if len(fila) != len(CABECERA_RECETAS):
                raise ArchivoInvalidoError(
                    f"La fila {numero_fila} no tiene 5 columnas"
                )
            try:
                receta = Receta(
                    int(fila[0]), fila[1], int(fila[2]), fila[3], fila[4]
                )
            except (ValueError, TypeError) as error:
                raise ArchivoInvalidoError(
                    f"Numero invalido en la fila {numero_fila}"
                ) from error
            libro.agregar(receta)

    return libro


def guardar_ingredientes_csv(ruta, ingredientes):
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerow(CABECERA_INGREDIENTES)
        escritor.writerows(ingredientes)


def cargar_ingredientes_csv(ruta):
    resultado = []

    with open(ruta, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=",")
        cabecera = next(lector, None)
        if cabecera != CABECERA_INGREDIENTES:
            raise ArchivoInvalidoError("Encabezado de ingredientes ausente o invalido")

        for numero_fila, fila in enumerate(lector, start=2):
            if len(fila) != len(CABECERA_INGREDIENTES):
                raise ArchivoInvalidoError(
                    f"La fila {numero_fila} no tiene 4 columnas"
                )
            try:
                receta_id = int(fila[0])
                cantidad = int(fila[2])

            except (ValueError, TypeError) as error:
                raise ArchivoInvalidoError(
                    f"Numero invalido en la fila {numero_fila}"
                ) from error

            resultado.append((receta_id, fila[1], cantidad, fila[3]))

    return resultado

# TEORIA : SI, hace falta leer los registros anteriores, el acceso a un archivo de texto es secuencial, no directo            
