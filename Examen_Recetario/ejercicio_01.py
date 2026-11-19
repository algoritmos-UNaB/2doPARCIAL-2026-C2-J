

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
# La identidad de la receta es el id y no debería poder cambiar después
# de construido el objeto: no.