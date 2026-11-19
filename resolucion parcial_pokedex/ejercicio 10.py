import struct
from pathlib import Path
from ejercicio_01 import Pokemon
from ejercicio_02 import Pokedex
from ejercicio_09 import ArchivoInvalidoError


FORMATO_ENCABEZADO = "<4scI"
FORMATO_REGISTRO = "<I20s12s12s4H"
TAM_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)
TAM_REGISTRO = struct.calcsize(FORMATO_REGISTRO)
MAGIA_ESPERADA = b"AYED"
TEMA_ESPERADO = b"P"


def _codificar_texto(texto: str, ancho: int) -> bytes:
    raw = texto.encode("utf-8")[:ancho]
    return raw.ljust(ancho, b"\x00")


def _decodificar_texto(raw: bytes) -> str:
    return raw.rstrip(b"\x00").decode("utf-8")


def _empaquetar_registro(pokemon: Pokemon) -> bytes:
    return struct.pack(
        FORMATO_REGISTRO,
        pokemon.id,
        _codificar_texto(pokemon.nombre, 20),
        _codificar_texto(pokemon.tipo1, 12),
        _codificar_texto(pokemon.tipo2, 12),
        pokemon.hp,
        pokemon.ataque,
        pokemon.defensa,
        pokemon.velocidad,
    )


def _desempaquetar_registro(datos: bytes) -> Pokemon:
    (
        id_pokemon,
        raw_nombre,
        raw_tipo1,
        raw_tipo2,
        hp,
        ataque,
        defensa,
        velocidad,
    ) = struct.unpack(FORMATO_REGISTRO, datos)

    return Pokemon(
        id=id_pokemon,
        nombre=_decodificar_texto(raw_nombre),
        tipo1=_decodificar_texto(raw_tipo1),
        tipo2=_decodificar_texto(raw_tipo2),
        hp=hp,
        ataque=ataque,
        defensa=defensa,
        velocidad=velocidad,
        generacion=1,
    )


def _leer_y_validar_encabezado(archivo) -> int:
    raw_encabezado = archivo.read(TAM_ENCABEZADO)
    if len(raw_encabezado) < TAM_ENCABEZADO:
        raise ArchivoInvalidoError("El archivo es mas corto que el encabezado.")

    magia, tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, raw_encabezado)
    if magia != MAGIA_ESPERADA or tema != TEMA_ESPERADO:
        raise ArchivoInvalidoError("Encabezado binario invalido.")

    return cantidad


def guardar_binario(ruta: str | Path, pokedex: Pokedex) -> None:
    pokemones = pokedex.listar()
    encabezado = struct.pack(FORMATO_ENCABEZADO, MAGIA_ESPERADA, TEMA_ESPERADO, len(pokemones))

    with open(ruta, mode="wb") as archivo:
        archivo.write(encabezado)
        for pokemon in pokemones:
            archivo.write(_empaquetar_registro(pokemon))


def cargar_binario(ruta: str | Path) -> Pokedex:
    try:
        with open(ruta, mode="rb") as archivo:
            cantidad = _leer_y_validar_encabezado(archivo)
            pokedex = Pokedex()

            for _ in range(cantidad):
                raw_registro = archivo.read(TAM_REGISTRO)
                if len(raw_registro) < TAM_REGISTRO:
                    raise ArchivoInvalidoError("El archivo binario esta truncado.")
                pokedex.agregar(_desempaquetar_registro(raw_registro))

            return pokedex
    except (OSError, struct.error, UnicodeDecodeError) as exc:
        raise ArchivoInvalidoError(f"No se pudo leer el archivo binario: {ruta}") from exc


def actualizar_registro(ruta: str | Path, posicion: int, pokemon: Pokemon) -> None:
    if posicion < 0:
        raise ArchivoInvalidoError("La posicion del registro no puede ser negativa.")

    try:
        with open(ruta, mode="r+b") as archivo:
            cantidad = _leer_y_validar_encabezado(archivo)
            if posicion >= cantidad:
                raise ArchivoInvalidoError("La posicion del registro esta fuera de rango.")

            offset = TAM_ENCABEZADO + posicion * TAM_REGISTRO
            archivo.seek(offset)
            archivo.write(_empaquetar_registro(pokemon))
    except (OSError, struct.error) as exc:
        raise ArchivoInvalidoError(f"No se pudo actualizar el archivo binario: {ruta}") from exc


# TEORIA: El tamano fijo del encabezado (9 bytes) y el tamano fijo de cada registro (56 bytes), junto con el indice posicion (desde 0), permiten calcular el byte de inicio mediante encabezado + posicion * tamano_registro