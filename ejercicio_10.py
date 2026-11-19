import struct

from ejercicio_01 import Pokemon
from ejercicio_02 import Pokedex
from ejercicio_09 import ArchivoInvalidoError


ENCABEZADO_FMT = "<4scI"
REGISTRO_FMT = "<I20s12s12s4H"

ENCABEZADO_SIZE = struct.calcsize(ENCABEZADO_FMT)
REGISTRO_SIZE = struct.calcsize(REGISTRO_FMT)

MAGIA_ESPERADA = b"AYED"
TEMA_ESPERADO = b"P"


def _codificar_cadena(texto, ancho):
    if texto is None:
        texto = ""
    raw = texto.encode("utf-8")[:ancho]
    return raw.ljust(ancho, b"\x00")


def _decodificar_cadena(raw):
    return raw.split(b"\x00", 1)[0].decode("utf-8")


def _empaquetar_pokemon(pokemon):
    return struct.pack(
        REGISTRO_FMT,
        pokemon.id,
        _codificar_cadena(pokemon.nombre, 20),
        _codificar_cadena(pokemon.tipo1, 12),
        _codificar_cadena(pokemon.tipo2, 12),
        pokemon.hp,
        pokemon.ataque,
        pokemon.defensa,
        pokemon.velocidad,
    )


def _desempaquetar_pokemon(datos):
    poke_id, nombre_b, tipo1_b, tipo2_b, hp, ataque, defensa, velocidad = struct.unpack(
        REGISTRO_FMT, datos
    )
    return Pokemon(
        poke_id,
        _decodificar_cadena(nombre_b),
        _decodificar_cadena(tipo1_b),
        _decodificar_cadena(tipo2_b),
        hp,
        ataque,
        defensa,
        velocidad,
        1,
    )


def guardar_binario(ruta, pokedex):
    pokemones = pokedex.listar()
    with open(ruta, "wb") as archivo:
        archivo.write(struct.pack(ENCABEZADO_FMT, MAGIA_ESPERADA, TEMA_ESPERADO, len(pokemones)))
        for pokemon in pokemones:
            archivo.write(_empaquetar_pokemon(pokemon))


def cargar_binario(ruta):
    with open(ruta, "rb") as archivo:
        encabezado_bytes = archivo.read(ENCABEZADO_SIZE)
        if len(encabezado_bytes) != ENCABEZADO_SIZE:
            raise ArchivoInvalidoError("Archivo binario más corto que el encabezado")

        magia, tema, cantidad = struct.unpack(ENCABEZADO_FMT, encabezado_bytes)
        if magia != MAGIA_ESPERADA or tema != TEMA_ESPERADO:
            raise ArchivoInvalidoError("Encabezado binario inválido")

        pokedex = Pokedex()
        for _ in range(cantidad):
            registro_bytes = archivo.read(REGISTRO_SIZE)
            if len(registro_bytes) != REGISTRO_SIZE:
                raise ArchivoInvalidoError("Archivo binario incompleto o truncado")
            pokedex.agregar(_desempaquetar_pokemon(registro_bytes))

    return pokedex


def actualizar_registro(ruta, posicion, pokemon):
    with open(ruta, "r+b") as archivo:
        encabezado_bytes = archivo.read(ENCABEZADO_SIZE)
        if len(encabezado_bytes) != ENCABEZADO_SIZE:
            raise ArchivoInvalidoError("Archivo binario más corto que el encabezado")

        magia, tema, cantidad = struct.unpack(ENCABEZADO_FMT, encabezado_bytes)
        if magia != MAGIA_ESPERADA or tema != TEMA_ESPERADO:
            raise ArchivoInvalidoError("Encabezado binario inválido")

        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError("Posición de registro fuera de rango")

        offset = ENCABEZADO_SIZE + posicion * REGISTRO_SIZE
        archivo.seek(offset)
        archivo.write(_empaquetar_pokemon(pokemon))


# TEORIA: El tamaño fijo en bytes del encabezado (9 bytes) y de cada registro (56 bytes), que permiten calcular el byte de inicio como 9 + posicion * 56.
