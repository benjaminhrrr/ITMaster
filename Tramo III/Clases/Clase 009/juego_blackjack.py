import utilidades as util
from mazos import MazoBlackJack
from role_BlackJack import Croupier, Player, Human, Entity


class BlackJack:
    def __init__(self) -> None:
        self.__croupier: Croupier = Croupier()
        self.__mazo: MazoBlackJack = MazoBlackJack()
        self.__jugadores: list[Player] = []
        self.__apuestas: list[int] = []

    @property
    def croupier(self) -> Croupier:
        return self.__croupier

    @property
    def mazo(self) -> MazoBlackJack:
        return self.__mazo

    @property
    def jugadores(self) -> list[Player]:
        return self.__jugadores

    @property
    def apuestas(self) -> list[int]:
        return self.__apuestas

    def agregar_jugador(self, player: Player) -> None:
        if not isinstance(player, Player):
            raise ValueError("Solo pueden jugar los clientes.")
        self.jugadores.append(player)

    def __hay_jugadores(self) -> bool:
        return len(self.jugadores) > 0

    def __juego_inicia_mano(self) -> None:
        self.mazo.barajar()
        self.apuestas.clear()

    def __jugadores_apuestan(self) -> None:
        print(self.croupier)
        for p in self.jugadores:
            self.apuestas.append(p.apostar())

    def __juego_reparte_dos_cartas(self) -> None:
        for p in self.jugadores:
            p.poner_carta(self.mazo.sacar_carta())
            p.poner_carta(self.mazo.sacar_carta())
        ct = self.mazo.sacar_carta()
        ct.tapar()
        self.croupier.poner_carta(ct)
        self.croupier.poner_carta(self.mazo.sacar_carta())

    def __jugadores_juegan(self) -> None:
        print(util.titulo("Juegan los clientes..."))
        print(self.croupier)
        for p in self.jugadores:
            while not p.plantarse():
                p.poner_carta(self.mazo.sacar_carta())

    def __croupier_juega(self) -> None:
        print(util.titulo("Juega el Croupier..."))
        c = self.croupier.sacar_carta()
        c.destapar()
        self.croupier.poner_carta(c, 0)
        while self.croupier.plantarse():
            self.croupier.poner_carta(self.mazo.sacar_carta())

    def __juego_reparte_premios(self) -> None:
        print(util.titulo("¡Se reparten los premios!"))
        suma_croupier = self.croupier.sumar_cartas()
        if suma_croupier > 21:  # SE PASÓ EL CROUPIER
            print(f"¡El {self.croupier} con {suma_croupier} fichas: se pasó!")
            for index, p in enumerate(self.jugadores):
                apuesta = self.apuestas[index]
                suma_jugador = p.sumar_cartas()
                if suma_jugador > 21:  # PIERDE
                    cartel = "perdió..."
                    p.perder_fichas(apuesta)
                else:  # GANA
                    cartel = "¡ganó!"
                    p.ganar_fichas(apuesta)
                print(f"{p} {cartel}")
        else:
            print(f"{self.croupier}: {suma_croupier}")
            for index, p in enumerate(self.jugadores):
                apuesta = self.apuestas[index]
                suma_jugador = p.sumar_cartas()
                if suma_jugador > 21:  # PIERDE
                    cartel = "perdió..."
                    p.perder_fichas(apuesta)
                elif suma_jugador < suma_croupier:  # GANA
                    cartel = "¡Perdió! El Croupier sumó más puntos."
                    p.perder_fichas(apuesta)
                elif suma_jugador > suma_croupier:
                    cartel = "¡Ganó! El Croupier sumó menos puntos."
                    p.ganar_fichas(apuesta)
                else:
                    cartel = "Empató."
                print(f"{p} {cartel}")

    def __jugadores_se_descartan(self) -> None:
        for p in self.jugadores:
            while p.tiene_cartas():
                self.mazo.poner_carta(p.sacar_carta())
        while self.croupier.tiene_cartas():
            self.mazo.poner_carta(self.croupier.sacar_carta())

    def __jugadores_se_retiran(self) -> None:
        index = 0
        while index < len(self.jugadores):
            p = self.jugadores[index]
            if p.fichas <= 0:
                print(f"{p.nombre} se retira del juego.")
                self.jugadores.pop(index)
            else:
                index += 1

    def jugar(self) -> None:
        self.mazo.llenar()
        while self.__hay_jugadores():
            self.__juego_inicia_mano()
            self.__juego_reparte_dos_cartas()
            self.__jugadores_apuestan()
            self.__jugadores_juegan()
            self.__croupier_juega()
            self.__juego_reparte_premios()
            self.__jugadores_se_descartan()
            self.__jugadores_se_retiran()


def main():
    jbj = BlackJack()
    jbj.agregar_jugador(Human("Mauri", 100))
    # jbj.agregar_jugador(Entity("Clara", 100))
    jbj.agregar_jugador(Human("Benja", 100))
    # jbj.agregar_jugador(Entity("Compucoso", 100))
    jbj.agregar_jugador(Human("Zoe", 100))

    jbj.jugar()


main()
