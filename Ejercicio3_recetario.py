from Ejercicio2_recetario import LibroRecetas, RecetaNoEncontrada


class SubrecetaFaltanteError(Exception):
    pass


class IngredienteFaltanteError(Exception):
    pass


def ingredientes_totales(receta_id, libro, subrecetas, ingredientes):
    libro.obtener(receta_id)
    resultado = []
    for r_id, nombre, cantidad, unidad in ingredientes:
        if r_id == receta_id:
            if nombre is None or nombre.strip() == "":
                raise IngredienteFaltanteError(f"Ingrediente sin nombre en la receta {receta_id}")
            resultado.append((nombre, cantidad, unidad))
    for r_id, sub_id in subrecetas:
        if r_id == receta_id:
            try:
                libro.obtener(sub_id)
            except RecetaNoEncontrada:
                raise SubrecetaFaltanteError(f"Falta la sub-receta {sub_id}")
            resultado.extend(ingredientes_totales(sub_id, libro, subrecetas, ingredientes))
    return resultado


# TEORIA
# Traza de ingredientes_totales(9):
# ingredientes_totales(9)
#   -> ingredientes_totales(1)   (caso base: sin sub-recetas)
#   -> ingredientes_totales(2)   (caso base: sin sub-recetas)