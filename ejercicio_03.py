from ejercicio_02 import Biblioteca, CancionNoEncontradaError


def versiones_de(biblioteca: Biblioteca, versiones: list, cancion_id: int) -> list:
    """Lista de (titulo, tipo) de todo lo derivado, sin incluir la canción original."""
    biblioteca.obtener(cancion_id)

    versiones_directas = [
        (cid, tipo)
        for cid, origen_id, tipo in versiones
        if origen_id == cancion_id
    ]
    versiones_directas.sort(key=lambda item: item[0])

    if not versiones_directas:
        return []

    resultado = []
    for cid, tipo in versiones_directas:
        cancion_derivada = biblioteca.obtener(cid)
        resultado.append((cancion_derivada.titulo, tipo))
        resultado.extend(versiones_de(biblioteca, versiones, cid))

    return resultado