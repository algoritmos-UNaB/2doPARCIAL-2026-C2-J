import csv
from pathlib import Path
from ejercicio_01 import Pokemon
from ejercicio_02 import Pokedex


ENCABEZADO_ESPERADO = [
    "id",
    "nombre",
    "tipo1",
    "tipo2",
    "hp",
    "ataque",
    "defensa",
    "velocidad",
    "generacion",
]


class ArchivoInvalidoError(Exception):
    pass


def guardar_csv(ruta: str | Path, pokedex: Pokedex) -> None:
    with open(ruta, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerow(ENCABEZADO_ESPERADO)
        for pokemon in pokedex.listar():
            escritor.writerow([
                pokemon.id,
                pokemon.nombre,
                pokemon.tipo1,
                pokemon.tipo2,
                pokemon.hp,
                pokemon.ataque,
                pokemon.defensa,
                pokemon.velocidad,
                pokemon.generacion,
            ])


def _parsear_fila_pokemon(fila: list[str]) -> Pokemon:
    if len(fila) != 9:
        raise ArchivoInvalidoError(f"La fila debe tener 9 columnas y tiene {len(fila)}.")

    try:
        id_pokemon = int(fila[0])
        hp = int(fila[4])
        ataque = int(fila[5])
        defensa = int(fila[6])
        velocidad = int(fila[7])
        generacion = int(fila[8])
    except ValueError as exc:
        raise ArchivoInvalidoError("Uno de los campos numericos no es valido.") from exc

    nombre = fila[1]
    tipo1 = fila[2]
    tipo2 = fila[3]

    return Pokemon(
        id=id_pokemon,
        nombre=nombre,
        tipo1=tipo1,
        tipo2=tipo2,
        hp=hp,
        ataque=ataque,
        defensa=defensa,
        velocidad=velocidad,
        generacion=generacion,
    )


def cargar_csv(ruta: str | Path) -> Pokedex:
    try:
        with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
            lector = csv.reader(archivo, delimiter=",")
            encabezado = next(lector, None)
            if encabezado != ENCABEZADO_ESPERADO:
                raise ArchivoInvalidoError("El encabezado del CSV no es valido o falta.")

            pokedex = Pokedex()
            for fila in lector:
                if not fila:
                    continue
                pokemon = _parsear_fila_pokemon(fila)
                pokedex.agregar(pokemon)

            return pokedex
    except OSError as exc:
        raise ArchivoInvalidoError(f"No se pudo leer el archivo: {ruta}") from exc


# TEORIA: Si, hace falta leer los anteriores porque el acceso en un archivo CSV de texto con registros de longitud variable es secuencial.