import os 
import struct
from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca

# Formato encabezado: 4s (magia), 1s (tema), I (cantidad) = 9bytes
# Formato registro: I (id), 40s (titulo), 40s (artista), 40s(album), 16s (genero), H (anio), H (duracion) = 144 bytes
FORMATO_ENCABEZADO = "=4s1sI"
FORMATO_REGISTRO = '=I40s40s40s16sHH'
MAGIA_ESPERADA = b"AYED"
TEMA_ESPERADO = b"M"


def _pack_cancion(c):
    return struct.pack(
        FMT_REG,
        c.id,
        c.titulo.encode("utf-8")[:40].ljust(40, b"\x00"),
        c.artista.encode("utf-8")[:40].ljust(40, b"\x00"),
        c.album.encode("utf-8")[:40].ljust(40, b"\x00"),
        c.genero.encode("utf-8")[:16].ljust(16, b"\x00"),
        c.anio,
        c.duracion_seg,
    )


def guardar_binario(ruta, biblioteca):
    with open(ruta, "wb") as f:
        f.write(struct.pack(FMT_HEADER, b"AYED", b"M", biblioteca.cantidad()))
        for cancion in biblioteca:
            f.write(_pack_cancion(cancion))


def cargar_binario(ruta):
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"No existe el archivo: {ruta}")

    with open(ruta, "rb") as f:
        header = f.read(9)
        if len(header) < 9:
            raise ArchivoInvalidoError("Archivo demasiado chico")

        magia, tema, cantidad = struct.unpack(FMT_HEADER, header)
        if magia != b"AYED" or tema != b"M" or os.path.getsize(ruta) != 9 + cantidad * 144:
            raise ArchivoInvalidoError("Archivo binario inválido o corrupto")

        biblioteca = Biblioteca()
        for _ in range(cantidad):
            cid, tit, art, alb, gen, anio, dur = struct.unpack(FMT_REG, f.read(144))
            biblioteca.agregar(Cancion(
                cid,
                tit.split(b"\x00", 1)[0].decode("utf-8"),
                art.split(b"\x00", 1)[0].decode("utf-8"),
                alb.split(b"\x00", 1)[0].decode("utf-8"),
                gen.split(b"\x00", 1)[0].decode("utf-8"),
                anio,
                dur,
            ))
        return biblioteca


def actualizar_registro(ruta, posicion, cancion):
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"No existe el archivo: {ruta}")

    with open(ruta, "r+b") as f:
        header = f.read(9)
        if len(header) < 9:
            raise ArchivoInvalidoError("Archivo demasiado chico")

        magia, tema, cantidad = struct.unpack(FMT_HEADER, header)
        if magia != b"AYED" or tema != b"M" or os.path.getsize(ruta) != 9 + cantidad * 144:
            raise ArchivoInvalidoError("Archivo binario inválido o corrupto")

        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError(f"Posición {posicion} fuera de rango")

        f.seek(9 + posicion * 144)
        f.write(_pack_cancion(cancion))

"""
La formula para calcular el byte ed inicio del registro en la posicion k es: byte_inicio = tam_encabezado + (k*tam_registro)

seria: byte_inicio = 9 + (k*144)

"""