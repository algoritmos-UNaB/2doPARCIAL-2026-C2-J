def valor_campo(receta, campo):
	if campo == "tiempo":
		return receta.tiempo_min

	if campo == "dificultad":
		dificultades = {
			"baja": 0,
			"media": 1,
			"alta": 2
		}

		return dificultades[receta.dificultad]


def ordenar_seleccion(recetas, campo, descendente):
	n = len(recetas)

	for i in range(n - 1):
		posicion = i

		for j in range(i + 1, n):
			valor_j = valor_campo(recetas[j], campo)
			valor_posicion = valor_campo(recetas[posicion], campo)

			if descendente:
				if valor_j > valor_posicion:
					posicion = j
			else:
				if valor_j < valor_posicion:
					posicion = j

		if posicion != i:
			recetas[i], recetas[posicion] = (
				recetas[posicion],
				recetas[i]
			)

	return recetas


def ordenar_insercion(recetas, campo, descendente):
	for i in range(1, len(recetas)):
		actual = recetas[i]
		j = i - 1

		while j >= 0:
			valor_actual = valor_campo(actual, campo)
			valor_anterior = valor_campo(recetas[j], campo)

			if descendente:
				debe_mover = valor_anterior < valor_actual
			else:
				debe_mover = valor_anterior > valor_actual

			if not debe_mover:
				break

			recetas[j + 1] = recetas[j]
			j -= 1

		recetas[j + 1] = actual

	return recetas


# TEORIA
# Inserción es estable porque conserva el orden relativo de los
# elementos que tienen la misma clave.