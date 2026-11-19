class RecetaNoEncontrada(Exception):
    pass


class LibroRecetas:
    def __init__(self):
        self._recetas = []

    def agregar(self, receta):
        for i, existente in enumerate(self._recetas):
            if existente.id == receta.id:
                self._recetas[i] = receta
                return
        self._recetas.append(receta)

    def obtener(self, id):
        for receta in self._recetas:
            if receta.id == id:
                return receta
        raise RecetaNoEncontrada(f"No existe la receta {id}")

    def listar(self):
        return list(self._recetas)

    def cantidad(self):
        return len(self._recetas)


# TEORIA
# Quien llama no puede ignorar sin querer el caso "no está": el error es explícito y se maneja con
# try/except, en lugar de recibir un None que recién falla más adelante en otra parte del código.