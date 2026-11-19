"""Ejercicio 3 - Versiones."""


def versiones_de(biblioteca, versiones, cancion_id) -> list:
    biblioteca.obtener(cancion_id)

    directas = []
    for v in versiones:
        if v[1] == cancion_id:
            directas.append(v)
    directas = sorted(directas)

    if not directas: # Caso Base
        return []

    resultado = []
    for id_version, _, tipo in directas: # Caso Recursivo
        titulo = biblioteca.obtener(id_version).titulo
        resultado.append((titulo, tipo))
        for par in versiones_de(biblioteca, versiones, id_version):
            resultado.append(par)
    return resultado


# TEORIA
# Caso base: si ninguna tupla tiene version_de_id == cancion_id, se devuelve [].
#
# Secuencia para versiones_de(..., 12):
#   versiones_de(12): directas = [13 live]
#     -> agrega ("Ji Ji Ji", "live") y llama a versiones_de(13)
#     versiones_de(13): directas = [70 remix]
#       -> agrega ("Ji Ji Ji (Remix)", "remix") y llama a versiones_de(70)
#       versiones_de(70): no hay directas (caso base) -> devuelve []
#     vuelve versiones_de(13) -> [("Ji Ji Ji (Remix)", "remix")]
#   vuelve versiones_de(12)
#     -> [("Ji Ji Ji", "live"), ("Ji Ji Ji (Remix)", "remix")]