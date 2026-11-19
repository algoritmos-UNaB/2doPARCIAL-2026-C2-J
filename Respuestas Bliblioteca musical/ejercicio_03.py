def versiones_de(biblioteca: Biblioteca, versiones: list, cancion_id: int) -> list:
    
    # Verifica la existencia de la cancion base en la biblioteca
    biblioteca.obtener(cancion_id)

    # Filtrar las versiones directas y ordenarlas por cancion_id ascendente
    directas = sorted(
        [v for v in versiones if v[6] == cancion_id],
        key=lambda x: x
    )

    resultado = []
    for v_id, _, tipo in directas:
        cancion_derivada = biblioteca.obtener(v_id)
        resultado.append((cancion_derivada.titulo, tipo))
        # Llamada recursiva para obtener las sub-versiones
        resultado.extend(versiones_de(biblioteca, versiones, v_id))

    return resultado
    
#RTA TEORIA:
# Caso Base: Ocurre cuando la cancion consultada no tiene versiones que deriven directamente de ella (directas = []), 
# devolviendo una lista vacia []