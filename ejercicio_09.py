import csv

from ejercicio_01 import Pokemon
from ejercicio_02 import Pokedex


class ArchivoInvalidoError(Exception):
    pass


ENCABEZADO = [
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


def guardar_csv(ruta, pokedex):
    with open(ruta, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerow(ENCABEZADO)
        for pokemon in pokedex.listar():
            escritor.writerow([
                pokemon.id,
                pokemon.nombre,
                pokemon.tipo1,
                pokemon.tipo2 if pokemon.tipo2 is not None else "",
                pokemon.hp,
                pokemon.ataque,
                pokemon.defensa,
                pokemon.velocidad,
                pokemon.generacion,
            ])


def cargar_csv(ruta):
    with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo, delimiter=",")
        filas = list(lector)

    if not filas or filas[0] != ENCABEZADO:
        raise ArchivoInvalidoError("El archivo CSV no tiene el encabezado esperado")

    pokedex = Pokedex()
    for fila in filas[1:]:
        if len(fila) != len(ENCABEZADO):
            raise ArchivoInvalidoError("Una fila del CSV no tiene 9 columnas")

        try:
            poke_id = int(fila[0])
            hp = int(fila[4])
            ataque = int(fila[5])
            defensa = int(fila[6])
            velocidad = int(fila[7])
            generacion = int(fila[8])
        except ValueError as exc:
            raise ArchivoInvalidoError("Error al convertir un campo numérico del CSV") from exc

        nombre = fila[1]
        tipo1 = fila[2]
        tipo2 = fila[3]
        pokedex.agregar(Pokemon(poke_id, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad, generacion))

    return pokedex


# TEORIA: Sí, hace falta avanzar por los anteriores porque en un CSV de texto cada línea puede medir distinto y el acceso es secuencial.
