from pathlib import Path
import struct

from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca


class ArchivoInvalidoError(Exception):
    pass


ENCABEZADO_STRUCT = struct.Struct("=4s1sI")
TAMANIO_ENCABEZADO = ENCABEZADO_STRUCT.size  # 9 bytes: 4 + 1 + 4

REGISTRO_STRUCT = struct.Struct("=I40s40s40s16sHH")
TAMANIO_REGISTRO = REGISTRO_STRUCT.size    # 144 bytes: 4 + 40 + 40 + 40 + 16 + 2 + 2

MAGIA_ESPERADA = b"AYED"
TEMA_ESPERADO = b"M"


def _codificar_campo_texto(texto: str, ancho: int) -> bytes:
    raw = texto.encode("utf-8")
    if len(raw) > ancho:
        raw = raw[:ancho]
    return raw.ljust(ancho, b"\x00")


def _decodificar_campo_texto(raw: bytes) -> str:
    sin_nulos = raw.split(b"\x00", 1)[0]
    return sin_nulos.decode("utf-8")


def _empaquetar_cancion(cancion: Cancion) -> bytes:
    return REGISTRO_STRUCT.pack(
        cancion.id,
        _codificar_campo_texto(cancion.titulo, 40),
        _codificar_campo_texto(cancion.artista, 40),
        _codificar_campo_texto(cancion.album, 40),
        _codificar_campo_texto(cancion.genero, 16),
        cancion.anio,
        cancion.duracion_seg,
    )


def _desempaquetar_cancion(datos: bytes) -> Cancion:
    cancion_id, raw_titulo, raw_artista, raw_album, raw_genero, anio, duracion_seg = (
        REGISTRO_STRUCT.unpack(datos)
    )
    return Cancion(
        id=cancion_id,
        titulo=_decodificar_campo_texto(raw_titulo),
        artista=_decodificar_campo_texto(raw_artista),
        album=_decodificar_campo_texto(raw_album),
        genero=_decodificar_campo_texto(raw_genero),
        anio=anio,
        duracion_seg=duracion_seg,
    )


def _leer_y_validar_encabezado(archivo) -> int:
    encabezado_bytes = archivo.read(TAMANIO_ENCABEZADO)
    if len(encabezado_bytes) != TAMANIO_ENCABEZADO:
        raise ArchivoInvalidoError("El archivo binario es demasiado corto o no tiene encabezado válido.")

    magia, tema, cantidad = ENCABEZADO_STRUCT.unpack(encabezado_bytes)
    if magia != MAGIA_ESPERADA:
        raise ArchivoInvalidoError(f"Firma mágica inválida: {magia!r}")
    if tema != TEMA_ESPERADO:
        raise ArchivoInvalidoError(f"Tema inválido en encabezado: {tema!r}")

    return cantidad


def guardar_binario(ruta, biblioteca: Biblioteca) -> None:
    ruta_path = Path(ruta)
    canciones = list(biblioteca)
    cantidad = len(canciones)

    try:
        with ruta_path.open("wb") as archivo:
            archivo.write(ENCABEZADO_STRUCT.pack(MAGIA_ESPERADA, TEMA_ESPERADO, cantidad))
            for cancion in canciones:
                archivo.write(_empaquetar_cancion(cancion))
    except OSError as exc:
        raise ArchivoInvalidoError(f"Error al escribir el archivo binario: {exc}") from exc


def cargar_binario(ruta) -> Biblioteca:
    ruta_path = Path(ruta)
    if not ruta_path.is_file():
        raise ArchivoInvalidoError(f"El archivo binario no existe: {ruta}")

    try:
        with ruta_path.open("rb") as archivo:
            cantidad = _leer_y_validar_encabezado(archivo)
            tamanio_esperado = TAMANIO_ENCABEZADO + cantidad * TAMANIO_REGISTRO

            archivo.seek(0, 2)
            tamanio_real = archivo.tell()
            if tamanio_real != tamanio_esperado:
                raise ArchivoInvalidoError(
                    f"Tamaño de archivo inválido: se esperaban {tamanio_esperado} bytes y hay {tamanio_real}."
                )

            archivo.seek(TAMANIO_ENCABEZADO)
            biblioteca = Biblioteca()
            for _ in range(cantidad):
                bloque = archivo.read(TAMANIO_REGISTRO)
                if len(bloque) != TAMANIO_REGISTRO:
                    raise ArchivoInvalidoError("Registro binario incompleto o truncado.")
                biblioteca.agregar(_desempaquetar_cancion(bloque))

            return biblioteca
    except struct.error as exc:
        raise ArchivoInvalidoError(f"Error al desempaquetar estructura binaria: {exc}") from exc
    except OSError as exc:
        raise ArchivoInvalidoError(f"Error al leer el archivo binario: {exc}") from exc


def actualizar_registro(ruta, posicion: int, cancion: Cancion) -> None:
    ruta_path = Path(ruta)
    if not ruta_path.is_file():
        raise ArchivoInvalidoError(f"El archivo binario no existe: {ruta}")

    try:
        with ruta_path.open("r+b") as archivo:
            cantidad = _leer_y_validar_encabezado(archivo)
            tamanio_esperado = TAMANIO_ENCABEZADO + cantidad * TAMANIO_REGISTRO

            archivo.seek(0, 2)
            tamanio_real = archivo.tell()
            if tamanio_real != tamanio_esperado:
                raise ArchivoInvalidoError(
                    f"Tamaño de archivo inválido: se esperaban {tamanio_esperado} bytes y hay {tamanio_real}."
                )

            if posicion < 0 or posicion >= cantidad:
                raise ArchivoInvalidoError(
                    f"Posición {posicion} fuera de rango para {cantidad} registros."
                )

            offset = TAMANIO_ENCABEZADO + posicion * TAMANIO_REGISTRO
            archivo.seek(offset)
            archivo.write(_empaquetar_cancion(cancion))
    except struct.error as exc:
        raise ArchivoInvalidoError(f"Error al empaquetar registro binario: {exc}") from exc
    except OSError as exc:
        raise ArchivoInvalidoError(f"Error al actualizar el archivo binario: {exc}") from exc


# Teoría:
# Sea E = 9 bytes el tamaño del encabezado y R = 144 bytes el tamaño de cada registro,
# el byte de inicio (0-based) del registro en posición k es:
# byte_inicio(k) = 9 + k * 144