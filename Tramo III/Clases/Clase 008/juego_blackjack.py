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
        return len(self.jugadores > 0)

    def __juego_inicia_mano(self) -> None:
        self.mazo.barajar()
        self.apuestas.clear()

    def __jugadores_apuestan() -> None:
        pass

    def __juego_reparte_dos_cartas() -> None:
        pass

    def __jugadores_juegan() -> None:
        pass

    def __juego_reparte_premios() -> None:
        pass

    def __jugadores_se_descartan() -> None:
        pass

    def __jugadores_se_retiran() -> None:
        pass

    def jugar(self) -> None:
        self.mazo.llenar()
        while self.__hay_jugadores():
            self.__juego_inicia_mano()
            self.__jugadores_apuestan()
            self.__juego_reparte_dos_cartas()
            self.__jugadores_juegan()
            self.__juego_reparte_premios()
            self.__jugadores_se_descartan()
            self.__jugadores_se_retiran()


def main():
    jbj = BlackJack()
    jbj.agregar_jugador(Human("Rosita", 100))
    jbj.agregar_jugador(Entity("Clara", 100))
    jbj.agregar_jugador(Human("Raul", 100))
    jbj.agregar_jugador(Entity("Compucoso", 100))

    jbj.jugar()


main()
