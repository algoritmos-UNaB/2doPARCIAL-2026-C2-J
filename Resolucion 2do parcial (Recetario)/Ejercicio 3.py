from ejercicio_02 import LibroRecetas, RecetaNoEncontrada


class SubrecetaFaltanteError(Exception):
    def __init__(self, subreceta_id):
        super().__init__(f"Falta la sub-receta con id {subreceta_id}")
        self.subreceta_id = subreceta_id


class IngredienteFaltanteError(Exception):
    def __init__(self, receta_id):
        super().__init__(f"Ingrediente sin nombre en la receta {receta_id}")
        self.receta_id = receta_id


def ingredientes_totales(receta_id, libro, subrecetas, ingredientes):
    libro.obtener(receta_id)

    resultado = []

    for fila_receta_id, nombre, cantidad, unidad in ingredientes:
        if fila_receta_id == receta_id:
            if nombre is None or str(nombre).strip() == "":
                raise IngredienteFaltanteError(receta_id)
            resultado.append((nombre, cantidad, unidad))

    for fila_receta_id, subreceta_id in subrecetas:
        if fila_receta_id == receta_id:
            try:
                libro.obtener(subreceta_id)
            except RecetaNoEncontrada:
                raise SubrecetaFaltanteError(subreceta_id)

            resultado.extend(
                ingredientes_totales(subreceta_id, libro, subrecetas, ingredientes)
            )

    return resultado



# TEORIA
# Traza de ingredientes_totales(9), por receta_id y en el orden en que entran:
#
#   ingredientes_totales(9)
#     agrega los propios de 9: vacio, chorizo
#     -> ingredientes_totales(1)   caso base: 1 no tiene sub-recetas
#                                  devuelve perejil, ajo
#     -> ingredientes_totales(2)   caso base: 2 no tiene sub-recetas
#                                  devuelve tomate, cebolla
#
# Orden de entrada: 9, 1, 2.