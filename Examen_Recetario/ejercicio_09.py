import csv

from ejercicio_01 import Receta
from ejercicio_02 import LibroRecetas


class ArchivoInvalidoError(Exception):
	pass


def guardar_recetas_csv(ruta, libro):
	with open(ruta, "w", encoding="utf-8", newline="") as archivo:
		escritor = csv.writer(archivo)

		escritor.writerow([
			"id",
			"nombre",
			"tiempo_min",
			"dificultad",
			"categoria"
		])


		for receta in libro.listar():
			escritor.writerow([
				receta.id,
				receta.nombre,
				receta.tiempo_min,
				receta.dificultad,
				receta.categoria
			])


def cargar_recetas_csv(ruta):
	libro = LibroRecetas()

	try:
		with open(ruta, "r", encoding="utf-8", newline="") as archivo:
			lector = csv.reader(archivo)

			try:
				encabezado = next(lector)
			except StopIteration:
				raise ArchivoInvalidoError("Archivo vacío")

			encabezado_correcto = [
				"id",
				"nombre",
				"tiempo_min",
				"dificultad",
				"categoria"
			]


			if encabezado != encabezado_correcto:
				raise ArchivoInvalidoError("Encabezado inválido")

			for fila in lector:
				if len(fila) != 5:
					raise ArchivoInvalidoError(
						"Cantidad de columnas inválida"
					)


				try:
					id = int(fila[0])
					tiempo_min = int(fila[2])
				except ValueError:
					raise ArchivoInvalidoError("Número inválido")

				receta = Receta(
					id,
					fila[1],
					tiempo_min,
					fila[3],
					fila[4]
				)

				libro.agregar(receta)

	except OSError:
		raise ArchivoInvalidoError("No se pudo abrir el archivo")

	return libro


def guardar_ingredientes_csv(ruta, ingredientes):
	with open(ruta, "w", encoding="utf-8", newline="") as archivo:
		escritor = csv.writer(archivo)

		escritor.writerow([
			"receta_id",
			"nombre",
			"cantidad",
			"unidad"
		])

		for ingrediente in ingredientes:
			escritor.writerow(ingrediente)


def cargar_ingredientes_csv(ruta):
	resultado = []

	try:
		with open(ruta, "r", encoding="utf-8", newline="") as archivo:
			lector = csv.reader(archivo)

			try:
				encabezado = next(lector)
			except StopIteration:
				raise ArchivoInvalidoError("Archivo vacío")

			encabezado_correcto = [
				"receta_id",
				"nombre",
				"cantidad",
				"unidad"
			]

			if encabezado != encabezado_correcto:
				raise ArchivoInvalidoError("Encabezado inválido")

			for fila in lector:
				if len(fila) != 4:
					raise ArchivoInvalidoError(
						"Cantidad de columnas inválida"
					)

				try:
					receta_id = int(fila[0])
					cantidad = float(fila[2])


					if cantidad.is_integer():
						cantidad = int(cantidad)

				except ValueError:
					raise ArchivoInvalidoError("Número inválido")

				resultado.append(
					(receta_id, fila[1], cantidad, fila[3])
				)

	except OSError:
		raise ArchivoInvalidoError("No se pudo abrir el archivo")

	return resultado


# No. Para leer el registro 10 hay que pasar por los anteriores.
# Es un acceso secuencial.