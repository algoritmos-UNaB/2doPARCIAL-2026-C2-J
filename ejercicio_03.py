from ejercicio_02 import Biblioteca, CancionNoEncontradaError

def versiones_de(biblioteca, versiones, cancion_id) -> list:
    biblioteca.obtener(cancion_id)
    directas = []
    for v_id, de_id, tipo in versiones:
        if de_id == cancion_id:
            directas.append((v_id, tipo))
    if len(directas) == 0:
        return []
    directas.sort()
    resultado = []
    for v_id, tipo in directas:
        cancion_version = biblioteca.obtener(v_id)
        resultado.append((cancion_version.titulo, tipo))
        sub_versiones = versiones_de(biblioteca, versiones, v_id)
        for sub in sub_versiones:
            resultado.append(sub)
    
    return resultado


"""
Caso Base: Cuando una cancion no tiene ninguna version, se devuelve lista vacia

Secuencia de llamadas de versiones_de(...,12):
    Detecta la version 13 ("en directo") y agrega la cancion ('Ji Ji Ji) y llama recursivamente a versiones_de(..., 13)

    esa nueva llamada detecta la version directa 70, agrega Ji Ji Ji remix y llama recursivamente a versiones_de(..., 70).

    esta ultima llamada al ver que nadie deriva de la 70 cae al caso base y retorna la lista vacia.

"""