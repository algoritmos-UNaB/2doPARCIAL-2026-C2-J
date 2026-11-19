import os
import struct

from ejercicio_01 import Receta
from ejercicio_02 import LibroRecetas
from ejercicio_09 import ArchivoInvalidoError

FORMATO_ENCABEZADO = "<4scI"
FORMATO_REGISTRO = "<I32sH8s16s"
TAMANIO_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)  
TAMANIO_REGISTRO = struct.calcsize(FORMATO_REGISTRO)      

MAGIA = b"AYED"
TEMA = b"R"


def _cadena_fija(texto, ancho):
    """UTF-8 recortado (sin cortar un carácter a la mitad) o rellenado con
    \\0 hasta el ancho del campo."""
    datos = texto.encode("utf-8")[:ancho]
    datos = datos.decode("utf-8", errors="ignore").encode("utf-8")
    return datos.ljust(ancho, b"\0")


def _leer_cadena(datos):
    try:
        return datos.rstrip(b"\0").decode("utf-8")
    except UnicodeDecodeError as error:
        raise ArchivoInvalidoError("Cadena con UTF-8 inválido") from error


def _empaquetar_registro(receta):
    return struct.pack(
        FORMATO_REGISTRO,
        receta.id,
        _cadena_fija(receta.nombre, 32),
        receta.tiempo_min,
        _cadena_fija(receta.dificultad, 8),
        _cadena_fija(receta.categoria, 16),
    )


def _desempaquetar_registro(datos):
    id_, nombre, tiempo_min, dificultad, categoria = struct.unpack(
        FORMATO_REGISTRO, datos)
    return Receta(id_, _leer_cadena(nombre), tiempo_min,
                  _leer_cadena(dificultad), _leer_cadena(categoria))


def _leer_encabezado(archivo):
    """Valida el encabezado y devuelve la cantidad de recetas."""
    datos = archivo.read(TAMANIO_ENCABEZADO)
    if len(datos) < TAMANIO_ENCABEZADO:
        raise ArchivoInvalidoError("El archivo es más corto que el encabezado")
    magia, _tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, datos)
    if magia != MAGIA:
        raise ArchivoInvalidoError("Magia inválida: no es un archivo AYED")
    return cantidad


def guardar_binario(ruta, libro):
    recetas = libro.listar()

    contenido = struct.pack(FORMATO_ENCABEZADO, MAGIA, TEMA, len(recetas))
    for receta in recetas:
        contenido += _empaquetar_registro(receta)
    with open(ruta, "wb") as archivo:
        archivo.write(contenido)


def cargar_binario(ruta):
    libro = LibroRecetas()
    with open(ruta, "rb") as archivo:
        cantidad = _leer_encabezado(archivo)
        for _ in range(cantidad):
            datos = archivo.read(TAMANIO_REGISTRO)
            if len(datos) < TAMANIO_REGISTRO:
                raise ArchivoInvalidoError("El archivo termina antes de lo esperado")
            libro.agregar(_desempaquetar_registro(datos))
    return libro


def actualizar_registro(ruta, posicion, receta):
    """Reescribe solo el registro `posicion` (desde 0); no toca el
    encabezado, así que la cantidad no cambia."""
    with open(ruta, "r+b") as archivo:
        cantidad = _leer_encabezado(archivo)
        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError(f"Posición fuera de rango: {posicion}")
        inicio = TAMANIO_ENCABEZADO + posicion * TAMANIO_REGISTRO
        if os.fstat(archivo.fileno()).st_size < inicio + TAMANIO_REGISTRO:
            raise ArchivoInvalidoError("El archivo termina antes de lo esperado")
        datos = _empaquetar_registro(receta)
        archivo.seek(inicio)
        archivo.write(datos)


# TEORIA
# El dato clave es que todos los registros miden lo mismo (62 bytes, tamaño
# fijo) y que el encabezado ocupa 9 bytes, por lo que el registro `posicion`
# empieza en el byte 9 + posicion * 62 y se accede de forma directa con seek.