import os
import struct

from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca
from ejercicio_09 import ArchivoInvalidoError


FORMATO_ENCABEZADO = "=4s1sI"              
FORMATO_REGISTRO = "=I40s40s40s16sHH"      
TAM_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)  
TAM_REGISTRO = struct.calcsize(FORMATO_REGISTRO)      
MAGIA = b"AYED"
TEMA = b"M"


def _a_bytes(texto, ancho):
    """UTF-8, recortado al ancho y completado con \\0."""
    datos = texto.encode("utf-8")[:ancho]
    return datos.ljust(ancho, b"\0")


def _a_texto(datos):
    """Corta en el primer \\0 y decodifica."""
    return datos.split(b"\0", 1)[0].decode("utf-8", errors="ignore")


def _empaquetar(c):
    return struct.pack(FORMATO_REGISTRO, c.id,
                       _a_bytes(c.titulo, 40), _a_bytes(c.artista, 40),
                       _a_bytes(c.album, 40), _a_bytes(c.genero, 16),
                       c.anio, c.duracion_seg)


def _leer_encabezado(archivo, ruta):
    """Valida magia, tema y tamaño total. Devuelve la cantidad."""
    datos = archivo.read(TAM_ENCABEZADO)
    if len(datos) < TAM_ENCABEZADO:
        raise ArchivoInvalidoError("El archivo es demasiado corto")
    magia, tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, datos)
    if magia != MAGIA:
        raise ArchivoInvalidoError("La magia no es AYED")
    if tema != TEMA:
        raise ArchivoInvalidoError("El tema no es M")
    if os.path.getsize(ruta) != TAM_ENCABEZADO + cantidad * TAM_REGISTRO:
        raise ArchivoInvalidoError("El tamaño del archivo no coincide con la cantidad")
    return cantidad


def guardar_binario(ruta, biblioteca):
    with open(ruta, "wb") as archivo:
        archivo.write(struct.pack(FORMATO_ENCABEZADO, MAGIA, TEMA, biblioteca.cantidad()))
        for c in biblioteca:
            archivo.write(_empaquetar(c))


def cargar_binario(ruta) -> Biblioteca:
    try:
        archivo = open(ruta, "rb")
    except FileNotFoundError:
        raise ArchivoInvalidoError(f"El archivo {ruta} no existe")
    with archivo:
        cantidad = _leer_encabezado(archivo, ruta)
        biblioteca = Biblioteca()
        for _ in range(cantidad):
            campos = struct.unpack(FORMATO_REGISTRO, archivo.read(TAM_REGISTRO))
            biblioteca.agregar(Cancion(campos[0], _a_texto(campos[1]), _a_texto(campos[2]),
                                       _a_texto(campos[3]), _a_texto(campos[4]),
                                       campos[5], campos[6]))
        return biblioteca


def actualizar_registro(ruta, posicion, cancion):
    try:
        archivo = open(ruta, "r+b")
    except FileNotFoundError:
        raise ArchivoInvalidoError(f"El archivo {ruta} no existe")
    with archivo:
        cantidad = _leer_encabezado(archivo, ruta)
        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError(f"La posición {posicion} está fuera de rango")
        archivo.seek(TAM_ENCABEZADO + posicion * TAM_REGISTRO)   
        archivo.write(_empaquetar(cancion))                       


if __name__ == "__main__":
    print("Encabezado:", TAM_ENCABEZADO, "bytes | Registro:", TAM_REGISTRO, "bytes")

    b = Biblioteca()
    b.agregar(Cancion(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota",
                      "Un baión para el ojo idiota", "Rock", 1988, 316))
    b.agregar(Cancion(30, "De Música Ligera", "Soda Stereo", "Canción animal", "Rock", 1990, 213))
    b.agregar(Cancion(20, "Alfonsina y el mar", "Mercedes Sosa", "Mujeres argentinas", "Folklore", 1969, 297))

    guardar_binario("canciones.bin", b)
    print("Tamaño del archivo:", os.path.getsize("canciones.bin"))  

    for linea in cargar_binario("canciones.bin").listar():
        print(" ", linea)

    actualizar_registro("canciones.bin", 1,
                        Cancion(7, "Muchacha", "Spinetta", "Artaud", "Rock", 1973, 186))
    print("Después de actualizar la posición 1:")
    for linea in cargar_binario("canciones.bin").listar():
        print(" ", linea)

    try:
        actualizar_registro("canciones.bin", 5, b.obtener(12))
    except ArchivoInvalidoError as e:
        print("Error:", e)
    try:
        cargar_binario("no_existe.bin")
    except ArchivoInvalidoError as e:
        print("Error:", e)

# TEORÍA:
# El registro de posición k (0-based) empieza en el byte:
#     inicio(k) = 9 + k * 144
# donde 9 es el tamaño del encabezado y 144 el tamaño de cada registro.
# Por ejemplo, el registro 0 empieza en el byte 9 y el registro 1 en el 153.
# Como todos los registros miden lo mismo, se puede saltar directo con seek()
# sin leer los anteriores (a diferencia del CSV del ejercicio 9).