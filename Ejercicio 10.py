import os
import struct

from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca
from ejercicio_09 import ArchivoInvalidoError

MAGIA = b"AYED"
TEMA = b"M"
FORMATO_ENCABEZADO = "=4s1sI"
FORMATO_REGISTRO = "=I40s40s40s16sHH"
TAM_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)  # 9
TAM_REGISTRO = struct.calcsize(FORMATO_REGISTRO)      # 144

def _texto_a_bytes(texto, ancho):
    # Recorta al ancho; struct completa con \0 los campos mas cortos.
    return texto.encode("utf-8")[:ancho]

def _bytes_a_texto(datos):
    # Corta en el primer \0.
    return datos.split(b"\0", 1)[0].decode("utf-8", errors="ignore")

def _empaquetar(cancion):
    return struct.pack(
        FORMATO_REGISTRO,
        cancion.id,
        _texto_a_bytes(cancion.titulo, 40),
        _texto_a_bytes(cancion.artista, 40),
        _texto_a_bytes(cancion.album, 40),
        _texto_a_bytes(cancion.genero, 16),
        cancion.anio,
        cancion.duracion_seg, )

def _desempaquetar(datos):
    id, titulo, artista, album, genero, anio, duracion = struct.unpack(FORMATO_REGISTRO, datos)
    return Cancion(id, _bytes_a_texto(titulo), _bytes_a_texto(artista),
                   _bytes_a_texto(album), _bytes_a_texto(genero), anio, duracion)

def _validar_y_obtener_cantidad(ruta):
    """Valida magia, tema y tamanio total del archivo. Devuelve la cantidad."""
    if not os.path.isfile(ruta):
        raise ArchivoInvalidoError(f"El archivo {ruta!r} no existe")
    tamanio = os.path.getsize(ruta)
    if tamanio < TAM_ENCABEZADO:
        raise ArchivoInvalidoError("El archivo es mas corto que el encabezado")
    with open(ruta, "rb") as archivo:
        magia, tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, archivo.read(TAM_ENCABEZADO))
    if magia != MAGIA:
        raise ArchivoInvalidoError("Magia invalida: se esperaba AYED")
    if tema != TEMA:
        raise ArchivoInvalidoError("Tema invalido: se esperaba M")
    esperado = TAM_ENCABEZADO + cantidad * TAM_REGISTRO
    if tamanio != esperado:
        raise ArchivoInvalidoError(
            f"Tamanio invalido: son {tamanio} bytes y se esperaban {esperado}")
    return cantidad

def guardar_binario(ruta, biblioteca):
    canciones = list(biblioteca)
    with open(ruta, "wb") as archivo:
        archivo.write(struct.pack(FORMATO_ENCABEZADO, MAGIA, TEMA, len(canciones)))
        for cancion in canciones:
            archivo.write(_empaquetar(cancion))

def cargar_binario(ruta):
    cantidad = _validar_y_obtener_cantidad(ruta)
    biblioteca = Biblioteca()
    with open(ruta, "rb") as archivo:
        archivo.seek(TAM_ENCABEZADO)
        for _ in range(cantidad):
            biblioteca.agregar(_desempaquetar(archivo.read(TAM_REGISTRO)))
    return biblioteca

def actualizar_registro(ruta, posicion, cancion):
    cantidad = _validar_y_obtener_cantidad(ruta)
    if posicion < 0 or posicion >= cantidad:
        raise ArchivoInvalidoError(
            f"Posicion {posicion} fuera de rango (hay {cantidad} registros)")
    with open(ruta, "r+b") as archivo:
        archivo.seek(TAM_ENCABEZADO + posicion * TAM_REGISTRO)
        archivo.write(_empaquetar(cancion))

# TEORIA
# El registro de posicion k (0-based) empieza en el byte:
# TAM_ENCABEZADO + k * TAM_REGISTRO  =  9 + k * 144
# Como todos los registros miden lo mismo, se salta directo con seek, sin leer
# los anteriores.
