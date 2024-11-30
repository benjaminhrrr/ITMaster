# Los atributos son privados y los métodos son públicos


class Gato:
    # MÉTODO CONSTRUCTOR
    def __init__(self, nombre="", edad=0, color="") -> None:
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def hacer_ruido(self) -> str:
        return f"{str(self.nombre)}: ... ¡Miauuu!"

    def __str__(self) -> str:
        return f"{self.nombre}\nEdad: {self.edad} años\nColor: {self.color}"


def main():
    g1 = Gato("Salem", 3, "Negro")
    print(type(g1))
    print(g1)
    print(g1.hacer_ruido())
    g2 = Gato("Haku", 3, "Blanco")
    print(type(g2))
    print(g2)
    print(g2.hacer_ruido())


main()
