import random


class Gesto:
    PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK = 1, 2, 3, 4, 5
    GESTOS = {
        PIEDRA: "piedra",
        PAPEL: "papel",
        TIJERA: "tijera",
        LAGARTO: "lagarto",
        SPOCK: "Spock",
    }

    def __init__(self):
        self.__valor = random.randint(1, 5)

    def get_valor(self):
        return self.__valor

    def __str__(self):
        return Gesto.GESTOS[self.__valor]


class Player:
    def __init__(self, name):
        self.__name = name
        self.__hand = None

    def get_nombre(self):
        return self.__name

    def get_mano(self):
        return self.__hand

    def hacer_gesto(self):
        self.__hand = Gesto()

    def __str__(self):
        return f"{self.get_nombre()} eligió {str(self.__hand)}."


class PiPaTiLaSpo:
    REGLAS = {
        (Gesto.TIJERA, Gesto.PAPEL): "La tijera corta el papel.",
        (Gesto.PAPEL, Gesto.PIEDRA): "El papel tapa la piedra.",
        (Gesto.PIEDRA, Gesto.LAGARTO): "La piedra aplasta al lagarto.",
        (Gesto.LAGARTO, Gesto.SPOCK): "El lagarto envenena a Spock.",
        (Gesto.SPOCK, Gesto.TIJERA): "Spock rompe la tijera.",
        (Gesto.TIJERA, Gesto.LAGARTO): "La tijera decapita al lagarto.",
        (Gesto.LAGARTO, Gesto.PAPEL): "El lagarto devora el papel.",
        (Gesto.PAPEL, Gesto.SPOCK): "El papel desautoriza a Spock.",
        (Gesto.SPOCK, Gesto.PIEDRA): "Spock vaporiza la piedra.",
        (Gesto.PIEDRA, Gesto.TIJERA): "La piedra aplasta la tijera.",
    }

    def __init__(self, p1_name, p2_name):
        self.__p1 = Player(p1_name)
        self.__p2 = Player(p2_name)

    def get_regla(self, gesto1, gesto2):
        if (gesto1, gesto2) in PiPaTiLaSpo.REGLAS:
            return PiPaTiLaSpo.REGLAS[(gesto1, gesto2)]
        if (gesto2, gesto1) in PiPaTiLaSpo.REGLAS:
            return PiPaTiLaSpo.REGLAS[(gesto2, gesto1)]
        return None

    def jugar(self):
        v_p1, v_p2, end = 0, 0, False
        print("¡Que empiece el juego!")
        while not end:
            self.__p1.hacer_gesto()
            self.__p2.hacer_gesto()
            g1 = self.__p1.get_mano().get_valor()
            g2 = self.__p2.get_mano().get_valor()
            regla = self.get_regla(g1, g2)
            print(self.__p1)
            print(self.__p2)
            if regla is None:
                print("Empate.")
            else:
                gr = self.__p1 if (g1, g2) in PiPaTiLaSpo.REGLAS else self.__p2
                print(f"{regla} {gr.get_nombre()} ganó la ronda.")
                if gr is self.__p1:
                    v_p1 += 1
                else:
                    v_p2 += 1
            if v_p1 == 2 or v_p2 == 2:
                end = True
        print(f"¡{gr.get_nombre()} ganó el juego!")


def main():
    juego = PiPaTiLaSpo("Benja", "Luli")
    juego.jugar()


if __name__ == "__main__":
    main()
