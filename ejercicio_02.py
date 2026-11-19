from ejercicio_01 import Cancion


class CancionNoEncontradaError(Exception):
    pass


class Biblioteca:
    def __init__(self):
        self.canciones = []

    def agregar(self, cancion):
        self.canciones.append(cancion)

    def cantidad(self):
        return len(self.canciones)

    def obtener(self, id):
        for cancion in self.canciones:
            if cancion.id == id:
                return cancion
        raise CancionNoEncontradaError(f"No existe una canción con id {id}")

    def listar(self):
        resultado = []
        for cancion in self.canciones:
            resultado.append(str(cancion))
        return resultado

    def __iter__(self):
        return iter(self.canciones)


if __name__ == "__main__":
    b = Biblioteca()
    b.agregar(Cancion(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota",
                      "Un baión para el ojo idiota", "Rock", 1988, 316))
    b.agregar(Cancion(7, "Muchacha", "Spinetta", "Artaud", "Rock", 1973, 186))

    print(b.cantidad())          # 2
    print(b.obtener(7))          # #7 Muchacha | Spinetta | 1973 | 3:06
    for linea in b.listar():
        print(linea)
    for c in b:
        print(c.titulo)          # Jijiji / Muchacha
    try:
        b.obtener(99)
    except CancionNoEncontradaError as e:
        print("Error:", e)       # Error: No existe una canción con id 99

# TEORÍA:
# La biblioteca guarda el catálogo completo de canciones, cada una una sola vez.
# Una playlist guarda solo una selección de esas canciones en un orden elegido
# (y puede repetirlas), sin ser dueña de ellas: las referencia desde la biblioteca. 