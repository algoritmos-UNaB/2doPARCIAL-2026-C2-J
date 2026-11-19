import struct

# Encabezado: 4s (magia) + 1s (tema) + I (cantidad) = 9 bytes
FORMATO_ENCABEZADO = "=4s1sI"
TAMANIO_ENCABEZADO = 9

# Registro: I + 40s + 40s + 40s + 16s + H + H = 144 bytes
FORMATO_REGISTRO = "=I40s40s40s16sHH"
TAMANIO_REGISTRO = 144

def guardar_binario(ruta: str, biblioteca: Biblioteca):
    with open(ruta, "wb") as f:
        # Escribir encabezado
        f.write(struct.pack(FORMATO_ENCABEZADO, b"AYED", b"M", biblioteca.cantidad()))
        # Escribir registros
        for c in biblioteca:
            reg_bytes = struct.pack(
                FORMATO_REGISTRO,
                c.id,
                c.titulo.encode("utf-8")[:40].ljust(40, b"\x00"),
                c.artista.encode("utf-8")[:40].ljust(40, b"\x00"),
                c.album.encode("utf-8")[:40].ljust(40, b"\x00"),
                c.genero.encode("utf-8")[:16].ljust(16, b"\x00"),
                c.anio,
                c.duracion_seg
            )
            f.write(reg_bytes)

def cargar_binario(ruta: str) -> Biblioteca:
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"El archivo '{ruta}' no existe.")

    tamanio_archivo = os.path.getsize(ruta)
    if tamanio_archivo < TAMANIO_ENCABEZADO:
        raise ArchivoInvalidoError("Tamaño de archivo invalido.")

    with open(ruta, "rb") as f:
        encabezado_bytes = f.read(TAMANIO_ENCABEZADO)
        magia, tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, encabezado_bytes)

        if magia != b"AYED" or tema != b"M":
            raise ArchivoInvalidoError("Magia o tema de archivo binario invalido.")

        if tamanio_archivo != TAMANIO_ENCABEZADO + cantidad * TAMANIO_REGISTRO:
            raise ArchivoInvalidoError("El archivo no coincide")

        biblioteca = Biblioteca()
        for _ in range(cantidad):
            reg_bytes = f.read(TAMANIO_REGISTRO)
            cid, tit, art, alb, gen, anio, dur = struct.unpack(FORMATO_REGISTRO, reg_bytes)

            c = Cancion(
                id=cid,
                titulo=tit.decode("utf-8").split("\x00"),
                artista=art.decode("utf-8").split("\x00"),
                album=alb.decode("utf-8").split("\x00"),
                genero=gen.decode("utf-8").split("\x00"),
                anio=anio,
                duracion_seg=dur
            )
            biblioteca.agregar(c)

    return biblioteca

def actualizar_registro(ruta: str, posicion: int, cancion: Cancion):
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"El archivo '{ruta}' no existe.")

    tamanio_archivo = os.path.getsize(ruta)
    with open(ruta, "r+b") as f:
        encabezado_bytes = f.read(TAMANIO_ENCABEZADO)
        magia, tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, encabezado_bytes)

        if magia != b"AYED" or tema != b"M":
            raise ArchivoInvalidoError("Magia o tema invalido.")

        if tamanio_archivo != TAMANIO_ENCABEZADO + cantidad * TAMANIO_REGISTRO:
            raise ArchivoInvalidoError("Tamaño de archivo inconsistente.")

        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError(f"La posicion {posicion} esta fuera de rango.")

        offset = TAMANIO_ENCABEZADO + posicion * TAMANIO_REGISTRO
        f.seek(offset)

        reg_bytes = struct.pack(
            FORMATO_REGISTRO,
            cancion.id,
            cancion.titulo.encode("utf-8")[:40].ljust(40, b"\x00"),
            cancion.artista.encode("utf-8")[:40].ljust(40, b"\x00"),
            cancion.album.encode("utf-8")[:40].ljust(40, b"\x00"),
            cancion.genero.encode("utf-8")[:16].ljust(16, b"\x00"),
            cancion.anio,
            cancion.duracion_seg
        )
        f.write(reg_bytes)

# Rta: Formula: byte = 9 + (k * 144); donde 9 corresponde a la longitud fija del encabezado en bytes y 
#144 al tamaño uniforme de cada registro.