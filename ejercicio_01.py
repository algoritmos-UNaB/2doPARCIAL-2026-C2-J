class Pokemon:
    def __init__(self, id, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad, generacion):
        self.id = id
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.generacion = generacion

    def __str__(self):
        if self.tipo2:
            return f"#{self.id} {self.nombre} ({self.tipo1}/{self.tipo2})"
        return f"#{self.id} {self.nombre} ({self.tipo1})"

    def __eq__(self, otro):
        if not isinstance(otro, Pokemon):
            return False
        return self.id == otro.id


# TEORIA: La identidad del Pokémon es su id y el resto de sus atributos son su estado, así que no debería cambiar después de construido porque __eq__ se basa en el id.
