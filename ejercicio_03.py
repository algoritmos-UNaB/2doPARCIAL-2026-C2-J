""""## Ejercicio 3 — Versiones (12 pts)

Implementar una función recursiva que lista las versiones derivadas de una canción 
    (cover, live, remix), también las versiones de esas versiones:

```python
def versiones_de(biblioteca, versiones, cancion_id) -> list:
    #Lista de (titulo, tipo) de todo lo derivado, sin incluir la canción original.
```

`versiones` es una lista de tuplas `(cancion_id, version_de_id, tipo)`.

- Caso base: nadie es versión de esta canción. El resultado es la lista vacía.
- Si hay varias versiones directas, recorrerlas de menor a mayor `cancion_id`.
- Cada llamada recursiva trae lo derivado de esa versión. 
    El resultado es preorden: primero la versión directa `(titulo, tipo)`, 
    después lo que cuelga de ella.
- Si `cancion_id` no está en la biblioteca, lanzar `CancionNoEncontradaError`.

Con los datos de prueba, Jijiji (12) tiene el vivo Ji Ji Ji (13) y,
     debajo, el remix (70). Gracias a la Vida de Violeta Parra (61)
      tiene el cover de Mercedes Sosa (16).

**Teoría.** Escribir el caso base y 
    la secuencia de llamadas de `versiones_de(..., 12)`, 
    indicando qué lista devuelve cada llamada al volver.

---"""
class CancionNoEncontradaError(Exception):
    def __init__(self , cancion_id):
        super().__init__(f"no existe cancion con  el id {cancion_id}")

def versiones_de(biblioteca , versiones, cancion_id):
    biblioteca.obtener(cancion_id)
    resultado = []
    derivadas = []

    for original_id , version_id , tipo in versiones:
        if original_id == cancion_id:
            derivadas.append((version_id , tipo))

    derivadas = sorted(derivadas)

    for version_id , tipo in derivadas:
        cancion_version = biblioteca.obtener(version_id)

        resultado.append((cancion_version.titulo, tipo))

        resultado.extends (versiones_de(biblioteca,versiones,version_id))
    return resultado

"""TEORIA: en el caso base cuando una cancion no tiene versiones derivadas. la funcio devuelve []
ejemplo delas llamadas: versiones_de (...,12) 
                            versiones_de(...,13)
                                versiones_de(..., 70)
los retornos serian:
                        versiones_De(...,70 ) devuelve []
                            versiones_de (...,12) devuelve [("ji ji ji Remix" , "remix")]
                                                             [("ji ji ji " , "Envivo")]
                            versiones_de (...,13) devuelve  [("ji ji ji Remix" , "remix")]"""