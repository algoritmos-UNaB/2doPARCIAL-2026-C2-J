from ejercicio_02 import RecetaNoEncontrada


class Nodo:
	def __init__(self, dato):
		self.dato = dato
		self.siguiente = None


class ListaEnlazada:
	def __init__(self):
		self.primero = None
		self.cantidad_elementos = 0

	def esta_vacia(self):
		return self.primero is None

	def tamanio(self):
		return self.cantidad_elementos

	def insertar_al_inicio(self, dato):
		nuevo = Nodo(dato)
		nuevo.siguiente = self.primero
		self.primero = nuevo
		self.cantidad_elementos += 1

	def insertar_al_final(self, dato):
		nuevo = Nodo(dato)

		if self.primero is None:
			self.primero = nuevo
		else:
			actual = self.primero

			while actual.siguiente is not None:
				actual = actual.siguiente

			actual.siguiente = nuevo

		self.cantidad_elementos += 1

	def quitar_primero(self):
		if self.esta_vacia():
			return None

		dato = self.primero.dato
		self.primero = self.primero.siguiente
		self.cantidad_elementos -= 1

		return dato

	def eliminar_donde(self, condicion):
		anterior = None
		actual = self.primero

		while actual is not None:
			if condicion(actual.dato):

				if anterior is None:
					self.primero = actual.siguiente
				else:
					anterior.siguiente = actual.siguiente

				self.cantidad_elementos -= 1
				return True

			anterior = actual
			actual = actual.siguiente

		return False

	def __iter__(self):
		actual = self.primero

		while actual is not None:
			yield actual.dato
			actual = actual.siguiente


class MenuSemanal:
	DIAS = [
		"lunes",
		"martes",
		"miercoles",
		"jueves",
		"viernes",
		"sabado",
		"domingo"
	]

	def __init__(self):
		self.menu = ListaEnlazada()

	def agregar(self, dia, receta):
		if dia not in self.DIAS:
			raise ValueError("Día inválido")

		for par in self.menu:
			if par[0] == dia:
				self.menu.eliminar_donde(
					lambda x: x[0] == dia
				)
				break

		self.menu.insertar_al_final((dia, receta))

	def quitar(self, dia):
		encontrado = self.menu.eliminar_donde(
			lambda x: x[0] == dia
		)

		if not encontrado:
			raise RecetaNoEncontrada("No hay receta para ese día")

	def receta_de(self, dia):
		for par in self.menu:
			if par[0] == dia:
				return par[1]

		raise RecetaNoEncontrada("No hay receta para ese día")

	def __iter__(self):
		return iter(self.menu)


# TEORIA
# La referencia al siguiente nodo está guardada en el nodo anterior,
# por lo que para eliminar el último hay que recorrer la lista hasta
# encontrar el penúltimo.