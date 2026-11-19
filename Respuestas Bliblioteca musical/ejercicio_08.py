def ordenar_por_anio_seleccion(canciones: list) -> list:
    """Seleccion de mayor a menor."""
    n = len(canciones)
    for i in range(n):
        idx_max = i
        for j in range(i + 1, n):
            if canciones[j].anio > canciones[idx_max].anio:
                idx_max = j
        canciones[i], canciones[idx_max] = canciones[idx_max], canciones[i]
    return canciones

def ordenar_por_duracion_insercion(canciones: list) -> list:
    """Insercion de menor a mayor."""
    n = len(canciones)
    for i in range(1, n):
        clave = canciones[i]
        j = i - 1
        while j >= 0 and canciones[j].duracion_seg > clave.duracion_seg:
            canciones[j + 1] = canciones[j]
            j -= 1
        canciones[j + 1] = clave
    return canciones

# Rta: El algoritmo de Insercion es estable y conserva el orden relativo original de los elementos con claves iguales, 
# mientras que Seleccion es inestable en su variante estandar debido a los intercambios a larga distancia.