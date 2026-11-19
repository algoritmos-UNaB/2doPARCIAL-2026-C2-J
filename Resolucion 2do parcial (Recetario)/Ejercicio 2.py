class RecetaNoEncontrada(Exception):
    def __init__(self, id):
        super().__init__(f"No existe la receta con id {id}")
        self.id = id


class LibroRecetas:
    def __init__(self):
        self._recetas = []

    def agregar(self, receta):
        for i in range(len(self._recetas)):
            if self._recetas[i].id == receta.id:
                self._recetas[i] = receta
                return
        self._recetas.append(receta)

    def obtener(self, id):
        for receta in self._recetas:
            if receta.id == id:
                return receta
        raise RecetaNoEncontrada(id)

    def listar(self):
        return list(self._recetas)

    def cantidad(self):
        return len(self._recetas)


# TEORIA
# Quien llama gana un fallo explícito e imposible de ignorar en el punto
# exacto del error, en vez de un None que puede pasar desapercibido y romper
# más adelante (por ejemplo con un AttributeError) lejos de su causa real.