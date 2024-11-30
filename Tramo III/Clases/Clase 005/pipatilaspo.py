import random


class Gesto:
    # Atributos de clase (constantes)
    PIEDRA = 1
    PAPEL = 2
    TIJERA = 3
    LAGARTO = 4
    SPOCK = 5

    GESTOS = {
        PIEDRA: "piedra",
        PAPEL: "papel",
        TIJERA: "tijera",
        LAGARTO: "lagarto",
        SPOCK: "Spock",
    }

    def __init__(self) -> None:
        self.__valor: int = self.__gesto_random()

    def __eq__(self, __value: object) -> bool:
        if __value is None or not isinstance(__value, Gesto):
            return False
        return self.__valor == __value.__valor

    def get_valor(self) -> int:
        return self.__valor

    def __gesto_random(self) -> int:
        return random.randint(Gesto.PIEDRA, Gesto.SPOCK)

    def __str__(self) -> str:
        return f"{Gesto.GESTOS[self.__valor]}"


class Player:
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__hand: Gesto = Gesto()

    def get_nombre(self) -> str:
        return self.__name

    def get_mano(self) -> Gesto:
        return self.__hand

    def hacer_gesto(self) -> None:
        self.__hand = Gesto()

    def __str__(self) -> str:
        return f"{self.get_nombre()} eligió {str(self.__hand)}"


class PiPaTiLaSpo:
    # Reglas
    REGLA1 = 1
    REGLA2 = 2
    REGLA3 = 3
    REGLA4 = 4
    REGLA5 = 5
    REGLA6 = 6
    REGLA7 = 7
    REGLA8 = 8
    REGLA9 = 9
    REGLA10 = 10

    REGLAS = {
        REGLA1: "La tijera corta el papel.",
        REGLA2: "El papel tapa la piedra.",
        REGLA3: "La piedra aplasta al lagarto.",
        REGLA4: "El lagarto envenena a Spock.",
        REGLA5: "Spock rompe la tijera.",
        REGLA6: "La tijera decapita al lagarto.",
        REGLA7: "El lagarto devora el papel.",
        REGLA8: "El papel desautoriza a Spock.",
        REGLA9: "Spock vaporiza la piedra.",
        REGLA10: "La piedra aplasta la tijera.",
    }

    def __init__(self, p1_name: str, p2_name: str) -> None:
        self.__p1: Player = Player(p1_name)
        self.__p2: Player = Player(p2_name)

    def __winner(self) -> Player:
        gesto1 = self.__p1.get_mano()
        gesto2 = self.__p2.get_mano()
        if gesto1 == gesto2:
            return None
        else:
            valor1 = gesto1.get_valor()
            valor2 = gesto2.get_valor()
            if (
                (valor1 == Gesto.TIJERA and valor2 == Gesto.PAPEL)
                or (valor1 == Gesto.PAPEL and valor2 == Gesto.PIEDRA)
                or (valor1 == Gesto.PIEDRA and valor2 == Gesto.LAGARTO)
                or (valor1 == Gesto.LAGARTO and valor2 == Gesto.SPOCK)
                or (valor1 == Gesto.SPOCK and valor2 == Gesto.TIJERA)
                or (valor1 == Gesto.TIJERA and valor2 == Gesto.LAGARTO)
                or (valor1 == Gesto.LAGARTO and valor2 == Gesto.PAPEL)
                or (valor1 == Gesto.PAPEL and valor2 == Gesto.SPOCK)
                or (valor1 == Gesto.SPOCK and valor2 == Gesto.PIEDRA)
                or (valor1 == Gesto.PIEDRA and valor2 == Gesto.TIJERA)
            ):
                return self.__p1
        return self.__p2

    def get_regla(self, gesto1, gesto2):
        gesto1 = self.__p1.get_mano()
        gesto2 = self.__p2.get_mano()
        if gesto1 == gesto2:
            return None
        else:
            valor1 = gesto1.get_valor()
            valor2 = gesto2.get_valor()
            if (valor1 == Gesto.TIJERA and valor2 == Gesto.PAPEL) or (
                valor2 == Gesto.TIJERA and valor1 == Gesto.PAPEL
            ):
                return PiPaTiLaSpo.REGLAS[PiPaTiLaSpo.REGLA1]
            elif (valor1 == Gesto.PAPEL and valor2 == Gesto.PIEDRA) or (
                valor2 == Gesto.PAPEL and valor1 == Gesto.PIEDRA
            ):
                return PiPaTiLaSpo.REGLAS[PiPaTiLaSpo.REGLA2]
            elif (valor1 == Gesto.PIEDRA and valor2 == Gesto.LAGARTO) or (
                valor2 == Gesto.PIEDRA and valor1 == Gesto.LAGARTO
            ):
                return PiPaTiLaSpo.REGLAS[PiPaTiLaSpo.REGLA3]
            elif (valor1 == Gesto.LAGARTO and valor2 == Gesto.SPOCK) or (
                valor2 == Gesto.LAGARTO and valor1 == Gesto.SPOCK
            ):
                return PiPaTiLaSpo.REGLAS[PiPaTiLaSpo.REGLA4]
            elif (valor1 == Gesto.SPOCK and valor2 == Gesto.TIJERA) or (
                valor2 == Gesto.SPOCK and valor1 == Gesto.TIJERA
            ):
                return PiPaTiLaSpo.REGLAS[PiPaTiLaSpo.REGLA5]
            elif (valor1 == Gesto.TIJERA and valor2 == Gesto.LAGARTO) or (
                valor2 == Gesto.TIJERA and valor1 == Gesto.LAGARTO
            ):
                return PiPaTiLaSpo.REGLAS[PiPaTiLaSpo.REGLA6]
            elif (valor1 == Gesto.LAGARTO and valor2 == Gesto.PAPEL) or (
                valor2 == Gesto.LAGARTO and valor1 == Gesto.PAPEL
            ):
                return PiPaTiLaSpo.REGLAS[PiPaTiLaSpo.REGLA7]
            elif (valor1 == Gesto.PAPEL and valor2 == Gesto.SPOCK) or (
                valor2 == Gesto.PAPEL and valor1 == Gesto.SPOCK
            ):
                return PiPaTiLaSpo.REGLAS[PiPaTiLaSpo.REGLA8]
            elif (valor1 == Gesto.SPOCK and valor2 == Gesto.PIEDRA) or (
                valor2 == Gesto.SPOCK and valor1 == Gesto.PIEDRA
            ):
                return PiPaTiLaSpo.REGLAS[PiPaTiLaSpo.REGLA9]
            elif (valor1 == Gesto.PIEDRA and valor2 == Gesto.TIJERA) or (
                valor2 == Gesto.PIEDRA and valor1 == Gesto.TIJERA
            ):
                return PiPaTiLaSpo.REGLAS[PiPaTiLaSpo.REGLA10]

    def jugar(self) -> None:
        victorias_p1 = 0
        victorias_p2 = 0
        end = False
        print("¡Que empiece el juego!")
        while not end:
            self.__p1.hacer_gesto()
            self.__p2.hacer_gesto()
            regla = self.get_regla(self.__p1.get_mano(), self.__p2.get_mano())
            print(self.__p1)
            print(self.__p2)
            ganador = self.__winner()
            if ganador is None:
                print("Empate.")
            elif ganador is self.__p1:
                print(f"{regla} {ganador.get_nombre()} ganó la ronda.")
                victorias_p1 += 1
            else:
                print(f"{regla} {ganador.get_nombre()} ganó la ronda.")
                victorias_p2 += 1
            if victorias_p1 == 2 or victorias_p2 == 2:
                end = True
        print(f"¡{ganador.get_nombre()} ganó el juego!")


def main():
    juego = PiPaTiLaSpo("Benja", "Zoe")
    juego.jugar()
    """
    for _ in range(10):
        print(Gesto())
    p1 = Player("Rosa")
    print(p1)
    p1.hacer_gesto()
    print(p1)
    print(Player("Pedro"))
    print(Player("Maria"))
    """


main()
