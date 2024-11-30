import utilidades as util
from abc import ABC, abstractmethod
from mazos import MazoBlackJack
from cartas import CartaPoker
from txtcolores import strclr


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

    def tiene_cartas(self) -> bool:
        return not self.mano.isvacio()

    def poner_carta(self, carta: CartaPoker, index: int = None) -> None:
        self.mano.poner_carta(carta, index)

    def sacar_carta(self, index: int = None) -> CartaPoker:
        return self.mano.sacar_carta(index)

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
        print(self)
        respuesta = False
        suma = self.sumar_cartas()
        if suma > 21:
            print(strclr("¡Se pasó!", "red"))
            respuesta = True
        elif suma >= 17:
            respuesta = True
        return respuesta


class BlackPlayer:
    pass


class Human(Player):
    def __init__(self, nombre: str, cantidad_fichas: int) -> None:
        super().__init__(nombre, cantidad_fichas)

    def apostar(self) -> int:
        print(self)
        return util.leer_entero("Apuesta: ", 1, self.fichas)

    def plantarse(self) -> bool:
        print(self)
        respuesta = False
        suma = self.sumar_cartas()
        if suma > 21:
            print(strclr("¡Se pasó!", "red"))
            respuesta = True
        elif suma == 21:
            respuesta = True
        else:
            respuesta = util.continua("¿Desea plantarse?")
        return respuesta


class Entity(Player):
    def __init__(self, nombre: str, cantidad_fichas: int) -> None:
        super().__init__(nombre, cantidad_fichas)

    def apostar(self) -> int:
        return super().apostar()

    def plantarse(self) -> bool:
        return super().plantarse()


#  Adapter
class AdaptadorAlien1(Player):
    def __init__(self, alien: BlackPlayer) -> None:
        nombre = alien.nombre
        fichas = alien.fichas
        super().__init__(nombre, fichas)

    def plantarse(self) -> bool:
        return super().plantarse()

    def apostar(self) -> int:
        return super().apostar()


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
