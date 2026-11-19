#Creo clase Receta
class Receta:
    def __init__(self, id, nombre, tiempo_min, dificultad, categoria ) :
        self.id = id
        self.nombre = nombre
        self.tiempo_min = tiempo_min
        self.dificultad = dificultad
        self.categoria = categoria

    def __str__(self):
        return f"#{self.id} {self.nombre} , {self.tiempo_min} min, {self.dificultad}, {self.categoria}"

    def __eq__(self, otro):
        if not isinstance(otro, Receta):
            return False
        return self.id == otro.id        

# TEORIA: el atributo ID es la identidad de la clase Receta, el resto de atributos son su estado. No, la identidad no deberia poder cambiarse, ya que perderia su caracter unico y tambien si se usa desde otras estructuras.