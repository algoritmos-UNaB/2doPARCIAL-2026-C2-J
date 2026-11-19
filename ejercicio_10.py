"""Ejercicio 10 — Registros binarios (9 pts)
Archivo binario de registros de longitud fija, con `struct` y formato estándar (`=`, sin padding de alineación).
Encabezado, 9 bytes: magia `4s` con `b"AYED"`, tema `1s` con `b"M"`, cantidad `I`.
Registro, 144 bytes:
| Campo | Formato |
| --- | --- |
| id | `I` |
| titulo | `40s` |
| artista | `40s` |
| album | `40s` |
| genero | `16s` |
| anio | `H` |
| duracion_seg | `H` |
Las cadenas van en UTF-8, recortadas al ancho y completadas con `\0`. Al leer, se corta en el primer `\0`. El artista más largo de los datos de prueba entra en 40 bytes.
```python
def guardar_binario(ruta, biblioteca): ...
def cargar_binario(ruta) -> Biblioteca: ...
def actualizar_registro(ruta, posicion, cancion): ...
```
`posicion` es 0-based. `actualizar_registro` escribe un solo registro en su lugar (`seek`) y no reescribe el resto del archivo. Lanza `ArchivoInvalidoError` si la magia no es `AYED`, si el tema no es `M`, si el archivo no cierra justo en `9 + cantidad * 144` bytes, o si `posicion` está fuera de rango.
**Teoría.** Escribir la fórmula del byte donde empieza el registro de posición `k`.
 Usar el tamaño del encabezado y el tamaño del registro."""

import struct
from pathlib import Path

ENCABEZADO_FMT = "=4s1sI"
ENCABEZADO_SIZE = struct.calcsize(ENCABEZADO_FMT)  
MAGIA_ESPERADA = b"AYED"
TEMA_ESPERADO = b"M"
REGISTRO_FMT = "=I40s40s40s16sHH"
REGISTRO_SIZE = struct.calcsize(REGISTRO_FMT)  


class ArchivoInvalidoError(Exception):
    def __init__(self, mensaje: str = "El archivo binario no es valido."):
        super().__init__(mensaje)


def _codificar_campo_texto(texto: str, ancho: int) -> bytes:
    partes = []
    usados = 0
    for ch in str(texto):
        b = ch.encode("utf-8")
        if usados + len(b) > ancho:
            break
        partes.append(b)
        usados += len(b)
    return b"".join(partes).ljust(ancho, b"\x00")

def _decodificar_campo_texto(datos: bytes) -> str:
    sin_nulos = datos.split(b"\x00", 1)[0]
    return sin_nulos.decode("utf-8")


def _empaquetar_cancion(cancion) -> bytes:
    return struct.pack(
        REGISTRO_FMT,
        int(cancion.id),
        _codificar_campo_texto(cancion.titulo, 40),
        _codificar_campo_texto(cancion.artista, 40),
        _codificar_campo_texto(cancion.album, 40),
        _codificar_campo_texto(cancion.genero, 16),
        int(cancion.anio),
        int(cancion.duracion_seg),
    )


def _desempaquetar_cancion(datos: bytes) -> "Cancion":
    c_id, raw_titulo, raw_artista, raw_album, raw_genero, anio, duracion_seg = struct.unpack(
        REGISTRO_FMT, datos
    )
    return Cancion(
        id=c_id,
        titulo=_decodificar_campo_texto(raw_titulo),
        artista=_decodificar_campo_texto(raw_artista),
        album=_decodificar_campo_texto(raw_album),
        genero=_decodificar_campo_texto(raw_genero),
        anio=anio,
        duracion_seg=duracion_seg,
    )

def _validar_y_leer_encabezado(archivo, tam_archivo: int) -> int:
    if tam_archivo < ENCABEZADO_SIZE:
        raise ArchivoInvalidoError("El archivo es mascorto que el encabezado de 9 bytes.")

    raw_enc = archivo.read(ENCABEZADO_SIZE)
    magia, tema, cantidad = struct.unpack(ENCABEZADO_FMT, raw_enc)

    if magia != MAGIA_ESPERADA:
        raise ArchivoInvalidoError(f"Magia invalida: se esperaba {MAGIA_ESPERADA!r}, se obtuvo {magia!r}.")
    if tema != TEMA_ESPERADO:
        raise ArchivoInvalidoError(f"Tema invalido: se esperaba {TEMA_ESPERADO!r}, se obtuvo {tema!r}.")

    tam_esperado = ENCABEZADO_SIZE + cantidad * REGISTRO_SIZE
    if tam_archivo != tam_esperado:
        raise ArchivoInvalidoError(
            f"Tamanioo invalido: se esperaban {tam_esperado} bytes para {cantidad} registros, pero hay {tam_archivo}."
        )
    return cantidad


def guardar_binario(ruta, biblioteca) -> None:
    canciones = list(biblioteca.canciones)
    ruta_path = Path(ruta)

    with ruta_path.open("wb") as archivo:
        archivo.write(struct.pack(ENCABEZADO_FMT, MAGIA_ESPERADA, TEMA_ESPERADO, len(canciones)))
        for cancion in canciones:
            archivo.write(_empaquetar_cancion(cancion))


def cargar_binario(ruta) -> "Biblioteca":
    ruta_path = Path(ruta)
    if not ruta_path.is_file():
        raise ArchivoInvalidoError(f"El archivo binario no existe: {ruta_path}")

    tam_archivo = ruta_path.stat().st_size
    canciones = []

    with ruta_path.open("rb") as archivo:
        cantidad = _validar_y_leer_encabezado(archivo, tam_archivo)
        for _ in range(cantidad):
            raw_reg = archivo.read(REGISTRO_SIZE)
            if len(raw_reg) != REGISTRO_SIZE:
                raise ArchivoInvalidoError("Registro incompleto al leer el archivo binario.")
            canciones.append(_desempaquetar_cancion(raw_reg))

    return Biblioteca(canciones)


def actualizar_registro(ruta, posicion: int, cancion) -> None:
    ruta_path = Path(ruta)
    if not ruta_path.is_file():
        raise ArchivoInvalidoError(f"El archivo binario no existe: {ruta_path}")

    tam_archivo = ruta_path.stat().st_size

    with ruta_path.open("r+b") as archivo:
        cantidad = _validar_y_leer_encabezado(archivo, tam_archivo)
        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError(
                f"Posicion {posicion} fuera de rango para un archivo con {cantidad} registros."
            )

        offset = ENCABEZADO_SIZE + posicion * REGISTRO_SIZE
        archivo.seek(offset)
        archivo.write(_empaquetar_cancion(cancion))
    """TEORIA:  9 + 144 * k (donde 9 es el encabezado y 144 es el tamanio de cada registro)."""