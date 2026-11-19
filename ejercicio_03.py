# ejercicio_03.py
from ejercicio_02 import Biblioteca, CancionNoEncontradaError


def versiones_de(biblioteca, versiones, cancion_id) -> list:
    """Lista de (titulo, tipo) de todo lo derivado, sin incluir la canción original."""
    # Lanza CancionNoEncontradaError si cancion_id no está en la biblioteca
    biblioteca.obtener(cancion_id)

    # Versiones directas de cancion_id, de menor a mayor cancion_id
    directas = sorted(
        (v for v in versiones if v[1] == cancion_id),
        key=lambda v: v[0],
    )

    # Caso base: sin versiones directas, el for no itera y se devuelve []
    resultado = []
    for id_version, _, tipo in directas:
        titulo = biblioteca.obtener(id_version).titulo
        resultado.append((titulo, tipo))                              # primero la versión directa
        resultado += versiones_de(biblioteca, versiones, id_version)  # después lo que cuelga de ella
    return resultado

"""Caso base: si nadie es versión de cancion_id, no hay versiones directas, el for no se ejecuta y la función devuelve [].
Secuencia de llamadas de versiones_de(..., 12):

versiones_de(12): la única versión directa es 13 (live). Agrega ("Ji Ji Ji", "live") y llama a versiones_de(13).
versiones_de(13): la única versión directa es 70 (remix). Agrega ("Ji Ji Ji (Remix)", "remix") y llama a versiones_de(70).
versiones_de(70): nadie es versión de 70, así que es el caso base y devuelve [].

Al volver seria: 
versiones_de(70) devuelve [].
versiones_de(13) devuelve [("Ji Ji Ji (Remix)", "remix")].
versiones_de(12) devuelve [("Ji Ji Ji", "live"), ("Ji Ji Ji (Remix)", "remix")]."""