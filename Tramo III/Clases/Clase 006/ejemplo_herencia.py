import math
from abc import ABC, abstractmethod


class Figura(ABC):
    def __init__(self, nombre) -> None:
        self.__nombre = nombre

    def get_nombre(self) -> str:
        return self.__nombre

    @abstractmethod
    def superficie(self) -> float:
        pass

    def __str__(self) -> str:
        return f"{self.__nombre} -> {self.superficie()}"


class Circulo(Figura):
    def __init__(self, radio) -> None:
        super().__init__("Círculo")
        self.__radio = radio

    def get_radio(self) -> float:
        return self.__radio

    def superficie(self) -> float:
        return math.pi * self.__radio**2


class Cuadrilatero(Figura):
    def __init__(self, nombre, l1, l2, l3, l4) -> None:
        super().__init__(nombre)
        self.__l1 = l1
        self.__l2 = l2
        self.__l3 = l3
        self.__l4 = l4

    def get_l1(self) -> float:
        return self.__l1

    def get_l2(self) -> float:
        return self.__l2

    def get_l3(self) -> float:
        return self.__l3

    def get_l4(self) -> float:
        return self.__l4

    def __str__(self) -> str:
        return f"{super().__str__()}. Lados: {self.__l1}, {self.__l2}, {self.__l3}, {self.__l4}"


class Cuadrado(Cuadrilatero):
    def __init__(self, lado) -> None:
        super().__init__("Cuadrado", lado, lado, lado, lado)

    def superficie(self) -> float:
        return self.get_l1() ** 2


class Rectangulo(Cuadrilatero):
    def __init__(self, L, lm) -> None:
        super().__init__("Rectangulo", lm, L, lm, L)

    def superficie(self) -> float:
        return self.get_l1() * self.get_l2()


class Triangulo(Figura):
    def __init__(self, b, h) -> None:
        super().__init__("Triangulo")
        self.__b = b
        self.__h = h

    def superficie(self) -> float | int:
        return self.__b * self.__h / 2

    def __str__(self) -> str:
        return f"{super().__str__()}. Base: {self.__b}. Altura: {self.__h}"


def main():
    lista = []
    lista.append(object())
    lista.append(Circulo(6))
    lista.append(Cuadrado(2))
    lista.append(Rectangulo(8, 3))
    lista.append(Triangulo(2, 3))
    for f in lista:
        print(f)


main()
