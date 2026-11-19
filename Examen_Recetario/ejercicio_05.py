from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
	pass

class Pila:
	def __init__(self):
		self.elementos = ListaEnlazada()

	def apilar(self, dato):
		self.elementos.insertar_al_inicio(dato)

	def desapilar(self):
		if self.esta_vacia():
			raise PilaVaciaError("La pila está vacía")

		return self.elementos.quitar_primero()


	def ver_tope(self):
		if self.esta_vacia():
			raise PilaVaciaError("La pila está vacía")

		for dato in self.elementos:
			return dato

	def esta_vacia(self):
		return self.elementos.esta_vacia()


class HistorialCocinado:
	def __init__(self):
		self.pila = Pila()

	def cocinar(self, receta):
		self.pila.apilar(receta)

	def deshacer(self):
		return self.pila.desapilar()

	def ultima(self):
		return self.pila.ver_tope()

# TEORIA
# Se apilan A, B y C. Después de desapilar una vez queda B en el tope.
# La disciplina se llama LIFO (Last In, First Out).