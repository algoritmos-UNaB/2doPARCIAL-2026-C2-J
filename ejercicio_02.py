from ejercicio_01. import Receta 

class RecetaNoEncontrada(exception) : 
    pass

class LibroRecetas : 
    def __init__ (self) :
        self.Recetas = []

    def agregar(self,Receta) :
        for indice, existente in ennumerate(self._Recetas) :
            if existente.id == Receta.id :
                self.Recetas[indice] = Receta
                return
                self._Recetas.append(Receta)
    
    def obtener(self, id) :
        for Receta in self._Recetas :
            if Receta.id == id :
                return Receta
                raise RecetaNoEncontrada (f"no se encontro la receta con id {id}")

    def listar(self) :
        return list (self._Recetas)  

    def cantidad(self) :
        return len (self._Recetas)  

# TEORIA: Quien llama al metodo tiene la garantia de que lo que recibe es una Receta valida                    