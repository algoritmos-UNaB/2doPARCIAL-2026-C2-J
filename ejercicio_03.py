from ejercicio_02 import RecetaNoEncontrada

class SubRecetaFaltanteError (exception) :
    pass

class IngredienteFaltanteError ( exception) :
    pass

def Ingredientes_Totales (receta_id, libro, subrecetas, ingredientes) :
    def expandir(id_actual, es_subreceta=False):
        try:
            libro.obtener(id_actual)
        except RecetaNoEncontrada as error:
            if es_subreceta:
                raise SubrecetaFaltanteError(
                    f"No existe la sub-receta con id {id_actual}"
                ) from error
            raise

        resultado = []

        for id_fila, nombre, cantidad, unidad in ingredientes:
            if id_fila == id_actual:
                if nombre is None or not str(nombre).strip():
                    raise IngredienteFaltanteError(
                        f"Ingrediente sin nombre en la receta {id_actual}"
                    )
                resultado.append((nombre, cantidad, unidad))

        for id_padre, id_hijo in subrecetas:
            if id_padre == id_actual:
                resultado.extend(expandir(id_hijo, es_subreceta=True))

        return resultado

    return expandir(receta_id)

# TEORIA : La traza es 9 -> 1 (caso base) -> 2 (caso base). En cada llamado se procesan primero los ingredientes propios y despues sus sub-recetas.
 