def busqueda_lineal(recetas, ingredientes, campo, valor):
	resultado = []

	for receta in recetas:

		if campo == "nombre":
			if receta.nombre == valor:
				resultado.append(receta)

		elif campo == "categoria":
			if receta.categoria == valor:
				resultado.append(receta)

		elif campo == "ingrediente":
			for ingrediente in ingredientes:
				id_receta = ingrediente[0]
				nombre = ingrediente[1]

				if id_receta == receta.id and nombre == valor:
					resultado.append(receta)
					break

	return resultado


def busqueda_binaria(recetas, campo, valor):
	inicio = 0
	fin = len(recetas) - 1

	while inicio <= fin:
		medio = (inicio + fin) // 2

		if campo == "nombre":
			nombre_medio = recetas[medio].nombre

			if nombre_medio == valor:
				return recetas[medio]

			elif nombre_medio < valor:
				inicio = medio + 1

			else:
				fin = medio - 1

	return None


# TEORIA
# No. La búsqueda binaria necesita que la lista esté ordenada por el
# mismo campo que se está buscando.