"""
Se pide implementar la clase Boleteria que recibe en su constructor un evento y
la cantidad de localidades para el mismo, de modo tal, que cumpla el siguiente
comportamiento:

>>> b1 = Boletería("Rush", 500)
>>> print(b1)
Evento: Rush - Localidades vendidas: 0 de 500
>>> b1.vender_localidades(400)
>>> b1.localidades_agotadas()
False
>>> b1.vender_localidades(100)
>>> b1.localidades_agotadas()
True
>>> b1.vender_localidades(200)
Traceback (most recent call last):
...
ValueError: No hay localidades suficientes.
>>> print(b1)
Evento: Rush - Localidades vendidas: 500 de 500
"""


class Boleteria:
    def __init__(self, nombre_evento: str, c_entradas: int) -> None:
        self.__nombre_evento: str = nombre_evento
        self.__c_entradas: int = c_entradas
        self.__vendidas: int = 0

    def getnombre_evento(self) -> str:
        return self.__nombre_evento

    def c_entradas(self) -> int:
        return self.__c_entradas

    def hay_lugar(self, c_entradas) -> bool:
        cantidad_disponible = self.__c_entradas - self.__vendidas
        return c_entradas <= cantidad_disponible

    def localidades_agotadas(self) -> bool:
        return self.__c_entradas == self.__vendidas

    def vender_entradas(self, cantidad_comprada: int) -> None:
        if not self.hay_lugar(cantidad_comprada):
            raise ValueError("No hay localidades suficientes.")
        self.__vendidas += cantidad_comprada

    def __str__(self) -> str:
        name = self.__nombre_evento
        sold = self.__vendidas
        seats = self.__c_entradas
        return f"Evento: {name} - Localidades vendidas: {sold} de {seats}"


class EmpresaDeEntradas:
    def __init__(self, nombre: str) -> None:
        self.__nombre: str = nombre
        self.__boleterias: list[Boleteria] = []

    def agregar_boleteria(self, boleteria: Boleteria) -> None:
        if boleteria is None or not isinstance(boleteria, Boleteria):
            raise ValueError("No se puede agregar si no es una boleteria.")
        self.__boleterias.append(boleteria)

    def vender_entradas(self, nombre_evento: str, c_entradas: int) -> None:
        evento_encontrado = self.__buscar_evento(nombre_evento)
        if evento_encontrado is None:
            print("No existe el evento.")
        elif evento_encontrado.localidades_agotadas():
            print("Localidades agotadas.")
        elif not evento_encontrado.hay_lugar(c_entradas):
            print("No hay localidades suficientes.")
        else:
            evento_encontrado.vender_entradas(c_entradas)
            print("Localidades vendidas.")

    def __buscar_evento(self, nombre_evento: str) -> Boleteria:
        for boleteria in self.__boleterias:
            if boleteria.getnombre_evento() == nombre_evento:
                return boleteria
        return None

    def __str__(self) -> str:
        boleterias = ", ".join(
            [boleteria.getnombre_evento() for boleteria in self.__boleterias]
        )
        return f"""
DETALLES
Empresa: {self.__nombre}
Eventos: {boleterias}"""


def main():
    e = EmpresaDeEntradas("Ticketon")

    print(str(e))

    b1 = Boleteria("Palito Ortega", 1000)
    b2 = Boleteria("Rush", 1000)
    b3 = Boleteria("Juan y Juan", 200)

    e.agregar_boleteria(b1)
    e.agregar_boleteria(b2)
    e.agregar_boleteria(b3)

    print(str(e))

    e.vender_entradas("Palito Ortega", 20)
    e.vender_entradas("Palito Ortega", 2000)
    e.vender_entradas("Rush", 20)
    e.vender_entradas("Rusha", 20)

    seats = b1.c_entradas()
    tickets = 2050

    try:
        b1.vender_entradas(tickets)
    except ValueError as e:
        print(f"Error: {e} Localidades: {seats}. Solicitadas: {tickets}")
    else:
        print(b1)

    b1.vender_entradas(15)
    print(b1)
    print(seats)


main()
