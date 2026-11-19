import struct
from ejercicio_01 import Receta
from ejercicio_02 import LibroRecetas
from ejercicio_09 import ArchivoInvalidoError

FORMATO_ENCABEZADO = "<4scI"
FORMATO_REGISTRO = "<I32sH8s16s"
TAMANIO_ENCABEZADO = 9   
TAMANIO_REGISTRO = 62    
MAGIA_ESPERADA = b"AYED"
TEMA_ESPERADO = b"R"


def _texto_a_bytes(texto, largo_fijo):
    datos = str(texto).encode("utf-8") [:largo_fijo]
    return datos.ljust(largo_fijo, b"\x00")


def _bytes_a_texto(datos) :

    sin_relleno = datos.split(b"\x00", 1)[0]
    try:
        return sin_relleno.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ArchivoInvalidoError("Texto invalido en el archivo binario") from error


def _empaquetar_receta(receta) :

    return struct.pack(
        FORMATO_REGISTRO,
        receta.id,
        _texto_a_bytes(receta.nombre, 32),
        receta.tiempo_min,
        _texto_a_bytes(receta.dificultad, 8),
        _texto_a_bytes(receta.categoria, 16),
    )


def _desempaquetar_receta(bloque_bytes):
    id_receta, bytes_nombre, tiempo_min, bytes_dificultad, bytes_categoria = struct.unpack(
        FORMATO_REGISTRO, bloque_bytes
    )
    return Receta(
        id_receta,
        _bytes_a_texto(bytes_nombre),
        tiempo_min,
        _bytes_a_texto(bytes_dificultad),
        _bytes_a_texto(bytes_categoria),
    )


def _leer_y_validar_encabezado(archivo):
    encabezado = archivo.read(TAMANIO_ENCABEZADO)
    if len(encabezado) < TAMANIO_ENCABEZADO:
        raise ArchivoInvalidoError("El archivo es mas corto que el encabezado")

    magia, tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, encabezado)

    if magia != MAGIA_ESPERADA or tema != TEMA_ESPERADO:
        raise ArchivoInvalidoError("Encabezado invalido: magia o tema incorrecto")

    return cantidad


def guardar_binario(ruta, libro ) :
    recetas = libro.listar()
    with open(ruta, "wb") as archivo:
        encabezado = struct.pack(FORMATO_ENCABEZADO, MAGIA_ESPERADA, TEMA_ESPERADO, len(recetas))
        archivo.write(encabezado)
        for receta in recetas:
            archivo.write(_empaquetar_receta(receta))


def cargar_binario(ruta) :
    libro = LibroRecetas()
    try:
        with open(ruta, "rb") as archivo:
            cantidad = _leer_y_validar_encabezado(archivo)
            for _ in range(cantidad):
                bloque = archivo.read(TAMANIO_REGISTRO)
                if len(bloque) < TAMANIO_REGISTRO:
                    raise ArchivoInvalidoError("Archivo incompleto: falta parte de un registro")

                libro.agregar(_desempaquetar_receta(bloque))

    except OSError as error:
        raise ArchivoInvalidoError("No se pudo abrir el archivo binario") from error

    return libro


def actualizar_registro(ruta, posicion, receta):
    try:
        with open(ruta, "r+b") as archivo:
            cantidad = _leer_y_validar_encabezado(archivo)

            if posicion < 0 or posicion >= cantidad:
                raise ArchivoInvalidoError("La posicion esta fuera de rango")

            desplazamiento = TAMANIO_ENCABEZADO + posicion * TAMANIO_REGISTRO

            archivo.seek(desplazamiento)
            archivo.write(_empaquetar_receta(receta))
    except OSError as error:
        raise ArchivoInvalidoError("No se pudo abrir el archivo binario") from error


# TEORIA: El tamanio fijo del registro (62 bytes) permite calcular el inicio: byte 9 + (posicion * 62), porque el encabezado ocupa 9 bytes.