from ejercicio_02 import Biblioteca, CancionNoEncontradaError

def versiones_de(biblioteca, versiones, cancion_id):
    """Lista de (titulo, tipo) de todo lo derivado, sin incluir la cancion original."""
    # Lanza CancionNoEncontradaError si cancion_id no esta en la biblioteca.
    biblioteca.obtener(cancion_id)

    # Versiones directas, de menor a mayor cancion_id.
    directas = sorted(
        (v for v in versiones if v[1] == cancion_id),
        key=lambda v: v[0], )
    # Caso base: sin versiones directas, el for no itera y devuelve [].
    resultado = []
    for version_id, _, tipo in directas:
        titulo = biblioteca.obtener(version_id).titulo
        resultado.append((titulo, tipo))                              # primero la version directa
        resultado += versiones_de(biblioteca, versiones, version_id)  # despues lo que cuelga de ella
    return resultado

# TEORIA
# Caso base: una cancion de la que nadie es version (no hay tuplas con
# version_de_id == cancion_id). Devuelve [].
#
# Secuencia de llamadas para versiones_de(..., 12):
# versiones_de(12)
# directas de 12: [13 (live)]
# -> versiones_de(13)
# directas de 13: [70 (remix)]
# -> versiones_de(70)
# directas de 70: ninguna -> caso base, devuelve []
# versiones_de(13) vuelve con [("Ji Ji Ji (Remix)", "remix")]
# versiones_de(12) vuelve con
# [("Ji Ji Ji", "live"), ("Ji Ji Ji (Remix)", "remix")]
