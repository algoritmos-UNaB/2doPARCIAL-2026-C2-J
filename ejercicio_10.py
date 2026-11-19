# ejercicio_10.py
import os
import struct
from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca
from ejercicio_09 import ArchivoInvalidoError

HEADER = struct.Struct("=4s1sI")                 # 9 bytes
REGISTRO = struct.Struct("=I40s40s40s16sHH")     # 144 bytes
MAGIA = b"AYED"
TEMA = b"M"


def _a_bytes(texto, ancho):
    return texto.encode("utf-8")[:ancho].ljust(ancho, b"\x00")


def _a_texto(datos):
    # Se corta en el primer \0. errors="ignore" por si el recorte a 40 bytes
    # partió un carácter multibyte al guardar.
    return datos.split(b"\x00")[0].decode("utf-8", errors="ignore")


def _cancion_a_tupla(c):
    return (
        c.id,
        _a_bytes(c.titulo, 40),
        _a_bytes(c.artista, 40),
        _a_bytes(c.album, 40),
        _a_bytes(c.genero, 16),
        c.anio,
        c.duracion_seg,
    )


def _tupla_a_cancion(t):
    return Cancion(t[0], _a_texto(t[1]), _a_texto(t[2]), _a_texto(t[3]),
                   _a_texto(t[4]), t[5], t[6])


def _validar(archivo, ruta):
    """Valida header y tamaño total. Devuelve la cantidad de registros."""
    cabecera = archivo.read(HEADER.size)
    if len(cabecera) < HEADER.size:
        raise ArchivoInvalidoError("Binario truncado: no tiene el encabezado completo.")
    magia, tema, cantidad = HEADER.unpack(cabecera)
    if magia != MAGIA:
        raise ArchivoInvalidoError(f"Magia incorrecta: {magia!r} (se esperaba {MAGIA!r}).")
    if tema != TEMA:
        raise ArchivoInvalidoError(f"Tema incorrecto: {tema!r} (se esperaba {TEMA!r}).")
    esperado = HEADER.size + cantidad * REGISTRO.size
    real = os.path.getsize(ruta)
    if real != esperado:
        raise ArchivoInvalidoError(
            f"Tamaño inválido: el archivo tiene {real} bytes y se esperaban {esperado}."
        )
    return cantidad


def _abrir(ruta, modo):
    try:
        return open(ruta, modo)
    except FileNotFoundError:
        raise ArchivoInvalidoError(f"El archivo {ruta!r} no existe.")


def guardar_binario(ruta, biblioteca):
    with open(ruta, "wb") as f:
        f.write(HEADER.pack(MAGIA, TEMA, biblioteca.cantidad()))
        for c in biblioteca:
            f.write(REGISTRO.pack(*_cancion_a_tupla(c)))


def cargar_binario(ruta) -> Biblioteca:
    with _abrir(ruta, "rb") as f:
        cantidad = _validar(f, ruta)
        biblioteca = Biblioteca()
        for _ in range(cantidad):
            datos = f.read(REGISTRO.size)
            biblioteca.agregar(_tupla_a_cancion(REGISTRO.unpack(datos)))
        return biblioteca


def actualizar_registro(ruta, posicion, cancion):
    """Pisa un solo registro con seek, sin reescribir el resto del archivo."""
    with _abrir(ruta, "r+b") as f:
        cantidad = _validar(f, ruta)
        if not isinstance(posicion, int) or not 0 <= posicion < cantidad:
            raise ArchivoInvalidoError(
                f"Posición {posicion} fuera de rango (0 a {cantidad - 1})."
            )
        f.seek(HEADER.size + posicion * REGISTRO.size)
        f.write(REGISTRO.pack(*_cancion_a_tupla(cancion)))


"""El registro de posición k empieza en el byte 9 + k × 144, es decir, tamaño del encabezado + k × tamaño del registro 
(con posiciones 0-based).
tipo por ejemplo el registro 0 empieza en el byte 9 y el registro 7 en el byte 9 + 7 × 144 = 1017."""


