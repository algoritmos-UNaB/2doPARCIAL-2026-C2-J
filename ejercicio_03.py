from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca, CancionNoEncontradaError


def versiones_de(biblioteca, versiones, cancion_id) -> list:
    """Lista de (titulo, tipo) de todo lo derivado, sin
    incluir la canción original."""
    # Si no existe, obtener() lanza CancionNoEncontradaError
    biblioteca.obtener(cancion_id)

    
    directas = []
    for v in versiones:
        if v[1] == cancion_id:          # v = (cancion_id, version_de_id, tipo)
            directas.append(v)

    
    if len(directas) == 0:
        return []

    
    directas = sorted(directas, key=lambda v: v[0])

    resultado = []
    for v in directas:
        version_id = v[0]
        tipo = v[2]
        titulo = biblioteca.obtener(version_id).titulo
        resultado.append((titulo, tipo))                              # primero la versión
        resultado += versiones_de(biblioteca, versiones, version_id)  # después lo que cuelga
    return resultado


if __name__ == "__main__":
    b = Biblioteca()
    b.agregar(Cancion(12, "Jijiji", "Patricio Rey", "Un baión", "Rock", 1988, 316))
    b.agregar(Cancion(13, "Ji Ji Ji", "Patricio Rey", "En vivo", "Rock", 1991, 330))
    b.agregar(Cancion(70, "Ji Ji Ji (Remix)", "DJ", "Remixes", "Electrónica", 2020, 280))
    b.agregar(Cancion(61, "Gracias a la Vida", "Violeta Parra", "Últimas", "Folklore", 1966, 270))
    b.agregar(Cancion(16, "Gracias a la Vida", "Mercedes Sosa", "Homenaje", "Folklore", 1971, 260))

    versiones = [
        (13, 12, "live"),
        (70, 13, "remix"),
        (16, 61, "cover"),
    ]

    print(versiones_de(b, versiones, 12))  # [('Ji Ji Ji', 'live'), ('Ji Ji Ji (Remix)', 'remix')]
    print(versiones_de(b, versiones, 61))  # [('Gracias a la Vida', 'cover')]
    print(versiones_de(b, versiones, 70))  # []
    try:
        versiones_de(b, versiones, 999)
    except CancionNoEncontradaError as e:
        print("Error:", e)

# TEORÍA:
# Caso base: si ninguna tupla tiene version_de_id == cancion_id, devuelve [].
# Secuencia de llamadas de versiones_de(..., 12):
#   versiones_de(12) -> encuentra 13 (live), agrega ('Ji Ji Ji','live') y llama a:
#     versiones_de(13) -> encuentra 70 (remix), agrega ('Ji Ji Ji (Remix)','remix') y llama a:
#       versiones_de(70) -> no tiene versiones: caso base, devuelve []
#     versiones_de(13) devuelve [('Ji Ji Ji (Remix)','remix')]
#   versiones_de(12) devuelve [('Ji Ji Ji','live'), ('Ji Ji Ji (Remix)','remix')]