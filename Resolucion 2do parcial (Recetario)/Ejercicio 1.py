class Receta:
    def __init__(self, id, nombre, tiempo_min, dificultad, categoria):
        self.id = id
        self.nombre = nombre
        self.tiempo_min = tiempo_min
        self.dificultad = dificultad
        self.categoria = categoria

    def __str__(self):
        return f"#{self.id} {self.nombre} – {self.tiempo_min} min, {self.dificultad}, {self.categoria}"

    def __eq__(self, other):
        if not isinstance(other, Receta):
            return False
        return self.id == other.id


# RESPUESTA TEORICA: El atributo id representa la identidad de la receta mientras que nombre, tiempo_min, dificultad y categoria representan su estado, y no debería poder cambiar después de construido el objeto porque rompería la unicidad e igualdad entre instancias.