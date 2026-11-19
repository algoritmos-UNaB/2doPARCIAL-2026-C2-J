class Pokemon:
    def __init__(
        self,
        id: int,
        nombre: str,
        tipo1: str,
        tipo2: str,
        hp: int,
        ataque: int,
        defensa: int,
        velocidad: int,
        generacion: int,
    ) -> None:
        self.id = int(id)
        self.nombre = str(nombre)
        self.tipo1 = str(tipo1)
        self.tipo2 = str(tipo2)
        self.hp = int(hp)
        self.ataque = int(ataque)
        self.defensa = int(defensa)
        self.velocidad = int(velocidad)
        self.generacion = int(generacion)

    def __str__(self) -> str:
        tipos = f"{self.tipo1}/{self.tipo2}" if self.tipo2 else self.tipo1
        return f"#{self.id} {self.nombre} ({tipos})"

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, Pokemon):
            return False
        return self.id == otro.id


# TEORIA: El atributo id es la identidad del Pokemon, mientras que nombre, tipo1, tipo2, hp, ataque, defensa, velocidad y generacion conforman su estado; no, la identidad no deberia poder cambiar despues de construir el objeto.