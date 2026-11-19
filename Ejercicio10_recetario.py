import struct

from Ejercicio1_recetario import Receta
from Ejercicio2_recetario import LibroRecetas
from Ejercicio9_recetario import ArchivoInvalidoError

FORMATO_ENCABEZADO = "<4scI"
FORMATO_REGISTRO = "<I32sH8s16s"
TAM_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)
TAM_REGISTRO = struct.calcsize(FORMATO_REGISTRO)


def _empaquetar(receta):
    return struct.pack(
        FORMATO_REGISTRO,
        receta.id,
        receta.nombre.encode("utf-8"),
        receta.tiempo_min,
        receta.dificultad.encode("utf-8"),
        receta.categoria.encode("utf-8"),
    )


def _texto(campo):
    return campo.rstrip(b"\0").decode("utf-8", errors="ignore")


def _leer_cantidad(f):
    datos = f.read(TAM_ENCABEZADO)
    if len(datos) < TAM_ENCABEZADO:
        raise ArchivoInvalidoError("Archivo más corto que el encabezado")
    magia, tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, datos)
    if magia != b"AYED":
        raise ArchivoInvalidoError("Magia inválida")
    return cantidad


def guardar_binario(ruta, libro):
    recetas = libro.listar()
    with open(ruta, "wb") as f:
        f.write(struct.pack(FORMATO_ENCABEZADO, b"AYED", b"R", len(recetas)))
        for receta in recetas:
            f.write(_empaquetar(receta))


def cargar_binario(ruta):
    libro = LibroRecetas()
    with open(ruta, "rb") as f:
        cantidad = _leer_cantidad(f)
        for _ in range(cantidad):
            datos = f.read(TAM_REGISTRO)
            if len(datos) < TAM_REGISTRO:
                raise ArchivoInvalidoError("Registro incompleto")
            id, nombre, tiempo, dificultad, categoria = struct.unpack(FORMATO_REGISTRO, datos)
            libro.agregar(Receta(id, _texto(nombre), tiempo, _texto(dificultad), _texto(categoria)))
    return libro


def actualizar_registro(ruta, posicion, receta):
    with open(ruta, "r+b") as f:
        cantidad = _leer_cantidad(f)
        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError("Posición fuera de rango")
        f.seek(TAM_ENCABEZADO + posicion * TAM_REGISTRO)
        f.write(_empaquetar(receta))


# TEORIA
# El tamaño fijo de cada registro (62 bytes) junto con el tamaño del encabezado (9 bytes):
# el registro empieza en el byte 9 + posicion * 62.