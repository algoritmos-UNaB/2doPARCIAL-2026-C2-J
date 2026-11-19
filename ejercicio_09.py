import os 
from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca

class ArchivoInvalidoError(Exception):
    pass

def guardar_cancion_csv(ruta, biblioteca):
    with open(ruta,'w', encoding="utf-8") as f:
        for c in biblioteca:
            linea = f'{c.id},{c.titulo},{c.artista},{c.album},{c.genero},{c.anio},{c.duracion_seg}\n'
            f.write(linea)

def cargar_canciones_csv(ruta): 
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f'El archivo no existe {ruta}')
    
    with open(ruta, "r", encoding="utf-8") as f:
        lineas = f.realines()
    if not lineas:
        raise ArchivoInvalidoError("El archivo no contiene encabezado")
    encabezado_esperado = "id,titulo,artista,album,genero,anio,duracion_seg"
    encabezado_archivo = lineas[0].strip()
    if encabezado_archivo != encabezado_esperado:
        raise ArchivoInvalidoError(f'Encabezado invalido: {encabezado_archivo}')
    biblioteca = Biblioteca()
    for num_linea, linea in enumerate(lineas[1:], start=2):
        linea_limpia = linea.strip()
        if not linea_limpia:
            continue
        columnas = linea_limpia.split(",")
        if len(columnas) < 7:
            raise ArchivoInvalidoError(f'Fila {num_linea} invalida, se esperaban 7 columnas y tiene {len(columnas)}')
        try:
            id_cancion = int(columnas[0])
            titulo = columnas[1]
            artista = columnas[2]
            album = columnas[3]
            genero = columnas[4]
            anio = int(columnas[5])
            duracion_seg = (columnas[6])
        except ValueError as e:
            raise ArchivoInvalidoError(f"Error de formato numerico en fila {num_fila}: {e}")
        cancion = Cancion(id_cancion, titulo, artista, album, genero, anio, duracion_seg)
        biblioteca.agregar(cancion)
    return biblioteca


"""
Para leer la cancion de la fila 50 es necesario recorrer las 49 filas anteriores pq el archivo CSV es de texto secuencial con lineas de longitud variable, por lo tanto no se puede saber en que posicion arranca la fila 50

"""