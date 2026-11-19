from ejercicio_01 import Cancion
from ejercicio_02 import CancionNoEncontradaError


class CampoInvalidoError(Exception):
    pass


CAMPOS_VALIDOS = ["titulo", "artista", "genero"]


def busqueda_lineal(canciones, campo, valor) -> list:
    if campo not in CAMPOS_VALIDOS:
        raise CampoInvalidoError(f"Campo inválido: {campo}")
    resultado = []
    for cancion in canciones:                     
        if getattr(cancion, campo) == valor:      
            resultado.append(cancion)
    return resultado


def busqueda_binaria_por_titulo(canciones_ordenadas, titulo) -> Cancion:
    inicio = 0
    fin = len(canciones_ordenadas) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        titulo_medio = canciones_ordenadas[medio].titulo
        if titulo_medio == titulo:
            return canciones_ordenadas[medio]
        elif titulo_medio < titulo:
            inicio = medio + 1      
        else:
            fin = medio - 1         
    raise CancionNoEncontradaError(f"No existe una canción titulada '{titulo}'")


if __name__ == "__main__":
    canciones = [
        Cancion(12, "Jijiji", "Patricio Rey", "Un baión", "Rock", 1988, 316),
        Cancion(30, "De Música Ligera", "Soda Stereo", "Canción animal", "Rock", 1990, 214),
        Cancion(20, "Alfonsina y el mar", "Mercedes Sosa", "Mujeres argentinas", "Folklore", 1969, 297),
        Cancion(31, "Persiana Americana", "Soda Stereo", "Signos", "Rock", 1986, 290),
        ]

    print("Rock:")
    for c in busqueda_lineal(canciones, "genero", "Rock"):
        print(" ", c)
    print("Soda Stereo:")
    for c in busqueda_lineal(canciones, "artista", "Soda Stereo"):
        print(" ", c)
    print(busqueda_lineal(canciones, "artista", "Spinetta"))   

    
    ordenadas = [canciones[2], canciones[1], canciones[0], canciones[3]]
    print(busqueda_binaria_por_titulo(ordenadas, "Jijiji"))
    try:
        busqueda_binaria_por_titulo(ordenadas, "Muchacha")
    except CancionNoEncontradaError as e:
        print("Error:", e)

# TEORÍA:
# La búsqueda binaria necesita la lista ordenada por título porque en cada paso
# compara con el elemento del medio y descarta la mitad donde seguro no está;
# eso solo es válido si los títulos están en orden. Su complejidad es O(log n).
# La búsqueda lineal por artista revisa las canciones una por una, así que en
# el peor caso recorre las n: complejidad O(n).