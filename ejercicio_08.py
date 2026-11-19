from ejercicio_01 import Cancion


def ordenar_por_anio_seleccion(canciones) -> list:
    """Selección. Año de mayor a menor."""
    n = len(canciones)
    for i in range(n - 1):
        pos_mayor = i
        for j in range(i + 1, n):                     
            if canciones[j].anio > canciones[pos_mayor].anio:
                pos_mayor = j
        
        canciones[i], canciones[pos_mayor] = canciones[pos_mayor], canciones[i]
    return canciones


def ordenar_por_duracion_insercion(canciones) -> list:
    """Inserción. duracion_seg de menor a mayor."""
    for i in range(1, len(canciones)):
        actual = canciones[i]
        j = i - 1
        
        while j >= 0 and canciones[j].duracion_seg > actual.duracion_seg:
            canciones[j + 1] = canciones[j]
            j -= 1
        canciones[j + 1] = actual                     
    return canciones


if __name__ == "__main__":
    canciones = [
        Cancion(12, "Jijiji", "Patricio Rey", "Un baión", "Rock", 1988, 316),
        Cancion(70, "Ji Ji Ji (Remix)", "DJ", "Remixes", "Electrónica", 2020, 280),
        Cancion(30, "De Música Ligera", "Soda Stereo", "Canción animal", "Rock", 1990, 213),
        Cancion(40, "En la ciudad de la furia (Unplugged)", "Soda Stereo", "Comfort y música para volar", "Rock", 1996, 345),
        Cancion(20, "Alfonsina y el mar", "Mercedes Sosa", "Mujeres argentinas", "Folklore", 1969, 297),
    ]

    print("Por año (mayor a menor):")
    for c in ordenar_por_anio_seleccion(canciones):
        print(" ", c)

    print("Por duración (menor a mayor):")
    for c in ordenar_por_duracion_insercion(canciones):
        print(" ", c)

# TEORÍA:
# Peor caso: selección es O(n^2) y inserción es O(n^2) (cuando la lista viene
# en orden inverso, cada elemento se corre hasta el principio).
# El que conserva el orden relativo de dos canciones con la misma clave
# (estable) es inserción: solo corre elementos estrictamente mayores (>), así
# que nunca pasa una canción por delante de otra igual. Selección no es
# estable, porque el intercambio puede saltear una canción por encima de otra
# con la misma clave.