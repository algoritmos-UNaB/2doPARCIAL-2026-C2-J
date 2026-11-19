
from ejercicio_01 import Receta
from ejercicio_02 import LibroRecetas, RecetaNoEncontrada

class SubrecetaFaltanteError(Exception):
	pass


class IngredienteFaltanteError(Exception):
	pass

def ingredientes_totales(receta_id, libro, subrecetas, ingredientes):

	if not any(receta.id == receta_id for receta in libro.listar()):
		raise RecetaNoEncontrada("Receta no encontrada")

	resultado = []

	# ptopios
	for ingrediente in ingredientes:
		id_ingrediente = ingrediente[0]
		nombre = ingrediente[1]
		cantidad = ingrediente[2]
		unidad = ingrediente[3]

		if id_ingrediente == receta_id:
			if nombre == "":
				raise IngredienteFaltanteError("Ingrediente faltante")

			resultado.append((nombre, cantidad, unidad))

    # Sub
	for relacion in subrecetas:
		id_receta = relacion[0]
		id_subreceta = relacion[1]

		if id_receta == receta_id:
			try:
				libro.obtener(id_subreceta)
			except RecetaNoEncontrada:
				raise SubrecetaFaltanteError("Subreceta faltante")

			resultado.extend(
				ingredientes_totales(
					id_subreceta,
					libro,
					subrecetas,
					ingredientes
				)
			)

	return resultado

# TEORIA
# Traza:
# ingredientes_totales(9)
#	-> ingredientes_totales(1)
#		-> caso base
#	-> ingredientes_totales(2)
#		-> caso base