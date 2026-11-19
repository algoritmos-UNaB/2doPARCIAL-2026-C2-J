from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
	pass


class Cola:
	def __init__(self):
		self.elementos = ListaEnlazada()

	def encolar(self, dato):
		self.elementos.insertar_al_final(dato)

	def desencolar(self):
		if self.esta_vacia():
			raise ColaVaciaError("La cola está vacía")

		return self.elementos.quitar_primero()

	def ver_frente(self):
		if self.esta_vacia():
			raise ColaVaciaError("La cola está vacía")

		for dato in self.elementos:
			return dato

	def esta_vacia(self):
		return self.elementos.esta_vacia()


class ColaPreparacion:
	def __init__(self):
		self.cola = Cola()

	def encolar(self, receta):
		self.cola.encolar(receta)

	def siguiente(self):
		return self.cola.desencolar()

	def proxima(self):
		return self.cola.ver_frente()


# TEORIA
# No devuelve C porque la cola utiliza la disciplina FIFO:
# First In, First Out.