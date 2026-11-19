import struct

from ejercicio_01 import Receta
from ejercicio_02 import LibroRecetas

class ArchivoInvalidoError(Exception):
	pass


FORMATO_ENCABEZADO = "<4scI"
FORMATO_REGISTRO = "<I32sH8s16s"

TAMANIO_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)
TAMANIO_REGISTRO = struct.calcsize(FORMATO_REGISTRO)


def convertir_cadena(texto, tamanio):
	datos = texto.encode("utf-8")

	if len(datos) > tamanio:
		datos = datos[:tamanio]

	return datos.ljust(tamanio, b"\0")


def guardar_binario(ruta, libro):
	recetas = libro.listar()
	
	with open(ruta, "wb") as archivo:
		archivo.write(
			struct.pack(
				FORMATO_ENCABEZADO,
				b"AYED",
				b"R",
				len(recetas)
			)
		)


		for receta in recetas:
			registro = struct.pack(
				FORMATO_REGISTRO,
				receta.id,
				convertir_cadena(receta.nombre, 32),
				receta.tiempo_min,
				convertir_cadena(receta.dificultad, 8),
				convertir_cadena(receta.categoria, 16)
			)

			archivo.write(registro)


def limpiar_cadena(datos):
	return datos.rstrip(b"\0").decode("utf-8")


def cargar_binario(ruta):
	with open(ruta, "rb") as archivo:
		datos_encabezado = archivo.read(TAMANIO_ENCABEZADO)

		if len(datos_encabezado) != TAMANIO_ENCABEZADO:
			raise ArchivoInvalidoError("Archivo demasiado corto")
		
		magia, tema, cantidad = struct.unpack(
			FORMATO_ENCABEZADO,
			datos_encabezado
		)

		if magia != b"AYED":
			raise ArchivoInvalidoError("Magia inválida")

		libro = LibroRecetas()

		for i in range(cantidad):
			datos_registro = archivo.read(TAMANIO_REGISTRO)

			if len(datos_registro) != TAMANIO_REGISTRO:
				raise ArchivoInvalidoError("Registro incompleto")

			id, nombre, tiempo, dificultad, categoria = struct.unpack(
				FORMATO_REGISTRO,
				datos_registro
			)

			receta = Receta(
				id,
				limpiar_cadena(nombre),
				tiempo,
				limpiar_cadena(dificultad),
				limpiar_cadena(categoria)
			)

			libro.agregar(receta)

		return libro


def actualizar_registro(ruta, posicion, receta):
	with open(ruta, "r+b") as archivo:
		datos_encabezado = archivo.read(TAMANIO_ENCABEZADO)

		if len(datos_encabezado) != TAMANIO_ENCABEZADO:
			raise ArchivoInvalidoError("Archivo demasiado corto")

		magia, tema, cantidad = struct.unpack(
			FORMATO_ENCABEZADO,
			datos_encabezado
		)
		if magia != b"AYED":
			raise ArchivoInvalidoError("Magia inválida")

		if posicion < 0 or posicion >= cantidad:
			raise ArchivoInvalidoError("Posición fuera de rango")

		desplazamiento = (
			TAMANIO_ENCABEZADO +
			posicion * TAMANIO_REGISTRO
		)

		archivo.seek(desplazamiento)

		registro = struct.pack(
			FORMATO_REGISTRO,
			receta.id,
			convertir_cadena(receta.nombre, 32),
			receta.tiempo_min,
			convertir_cadena(receta.dificultad, 8),
			convertir_cadena(receta.categoria, 16)
		)

		archivo.write(registro)


# TEORIA
# El tamaño fijo del registro permite calcular:
# desplazamiento = tamaño_encabezado + posicion * tamaño_registro