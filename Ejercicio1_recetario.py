class Receta:
    def __init__(self, id, nombre, tiempo_min, dificultad, categoria):
        self.id = id
        self.nombre = nombre
        self.tiempo_min = tiempo_min
        self.dificultad = dificultad
        self.categoria = categoria

    def __str__(self):
        return f"#{self.id} {self.nombre} — {self.tiempo_min} min, {self.dificultad}, {self.categoria}"

    def __eq__(self, otro):
        return isinstance(otro, Receta) and self.id == otro.id


# TEORIA
# La identidad es el atributo id: es lo que distingue a una receta de otra, y por eso __eq__ compara
# solo el id (dos recetas con el mismo id son la misma aunque el resto de los datos sea distinto).
# El estado son los demás atributos (nombre, tiempo_min, dificultad y categoria): pueden cambiar
# y la receta sigue siendo la misma.
# ¿La identidad debería poder cambiar después de construido el objeto? No.