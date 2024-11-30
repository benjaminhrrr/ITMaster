from abc import ABC, abstractmethod
from mazos import MazoBlackJack
from cartas import Carta, CartaPoker


# Una interfaz. Se utiliza para provocar herencia y comportamiento.
class Plantar(ABC):
    @abstractmethod
    def plantarse(self) -> bool:
        pass


class Apostar(ABC):
    @abstractmethod
    def apostar(self) -> int:
        pass


class RoleBlackJack(Plantar):
    def __init__(self, nombre: str) -> None:
        super().__init__()
        self.__nombre: str = nombre
        self.__mano: MazoBlackJack = MazoBlackJack()

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def mano(self) -> MazoBlackJack:
        return self.__mano

    def __str__(self) -> str:
        return f"{self.nombre} {self.mano}"

    def poner_carta(self, carta: CartaPoker, index: int = None) -> None:
        self.mano.poner_carta(carta, index)

    def sacar_carta(self, carta: Carta, index: int = None) -> CartaPoker:
        self.mano.poner_carta(carta, index)

    def sumar_cartas(self) -> int:
        cantidad_unos = 0
        suma_numeros = 0
        for carta in self.mano.cartas:
            if carta.numero == 1:
                cantidad_unos += 1
            elif carta.numero <= 10:
                suma_numeros += carta.numero
            else:
                suma_numeros += 10
        suma = 0
        if cantidad_unos == 0:
            suma = suma_numeros
        elif cantidad_unos == 1:
            if suma_numeros + 11 > 21:
                suma = suma_numeros + 1
            else:
                suma = suma_numeros + 11
        else:
            if suma_numeros + 11 + cantidad_unos - 1 > 21:
                suma = suma_numeros + cantidad_unos
            else:
                suma = suma_numeros + 11 + cantidad_unos - 1
        return suma


class Player(RoleBlackJack, Apostar):
    def __init__(self, nombre: str, cantidad_fichas: int) -> None:
        super().__init__(nombre)
        self.__fichas: int = cantidad_fichas

    @property
    def fichas(self) -> int:
        return self.__fichas

    def __str__(self) -> str:
        return f"{super().__str__()} - ${self.fichas} - {self.sumar_cartas()}"

    def ganar_fichas(self, cantidad: int) -> None:
        self.__fichas += cantidad

    def perder_fichas(self, cantidad: int) -> None:
        self.__fichas -= cantidad


class Croupier(RoleBlackJack):
    def __init__(self) -> None:
        super().__init__("Sr. Croupier")

    def plantarse(self) -> bool:
        pass


class Human(Player):
    def __init__(self, nombre: str, cantidad_fichas: int) -> None:
        super().__init__(nombre, cantidad_fichas)

    def apostar(self) -> int:
        return super().apostar()

    def plantarse(self) -> bool:
        return super().plantarse()


class Entity(Player):
    def __init__(self, nombre: str, cantidad_fichas: int) -> None:
        super().__init__(nombre, cantidad_fichas)

    def apostar(self) -> int:
        return super().apostar()

    def plantarse(self) -> bool:
        return super().plantarse()


if __name__ == "__main__":
    m = MazoBlackJack()
    m.llenar()
    m.barajar()
    cr = Croupier()
    x = m.sacar_carta()
    x.tapar()
    cr.poner_carta(x)
    cr.poner_carta(m.sacar_carta())
    print(cr)
    h = Human("Juan", 10)
    h.poner_carta(m.sacar_carta())
    h.poner_carta(m.sacar_carta())
    print(h)
