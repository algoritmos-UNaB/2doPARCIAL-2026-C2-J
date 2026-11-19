def descendientes(origen_id, pokedex, aristas):
    pokedex.obtener(origen_id)

    resultado = []
    for orig, dest in aristas:
        if orig == origen_id:
            pokedex.obtener(dest)
            resultado.append(dest)
            resultado.extend(descendientes(dest, pokedex, aristas))
    return resultado


# TEORIA: Entra primero descendientes(4), después descendientes(5) y por último descendientes(6), que es el caso base porque no tiene destinos y devuelve [].
