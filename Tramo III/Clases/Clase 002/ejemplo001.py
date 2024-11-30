"""
Implementar la clase Caramelera, que recibe en su constructor la cantidad de
caramelos que puede contener y tiene el siguiente comportamiento:

>>> c = Caramelera(20)
>>> c.sacar_caramelos(50)
Traceback (most recent call last):
...
ValueError: ¡No hay caramelos!
>>> c.poner_caramelos(10)
>>> c.sacar_caramelos(4)
>>> c.poner_caramelos(50)
Traceback (most recent call last):
...
ValueError: No hay lugar para tantos caramelos.
>>> print(c)
Caramelera con 6/20 caramelos.
"""


class Caramelera:
    def __init__(self, capacidad: int) -> None:
        if not capacidad:
            raise ValueError("No puede crear caramelera sin cantidad inicial")
        self.__capacidad = capacidad
        self.__cantidad = 0

    def poner_caramelos(self, cantidad: int) -> None:
        if not cantidad or cantidad < 0:
            raise ValueError("¡No puede agregar esa cantidad!")
        if self.__capacidad < self.__cantidad + cantidad:
            raise ValueError("¡No queda espacio para tantos caramelos!")
        self.__cantidad += cantidad

    def sacar_caramelos(self, cantidad: int) -> None:
        if not cantidad or cantidad < 0:
            raise ValueError("¡No puede sacar esa cantidad!")
        if cantidad > self.__cantidad:
            raise ValueError("¡No hay suficientes caramelos para sacar!")
        self.__cantidad -= cantidad

    def __len__(self) -> int:
        return self.__cantidad

    def __str__(self) -> str:
        return f"Caramelera: {self.__cantidad}/{self.__capacidad} caramelos."


def main():
    c = Caramelera(25)
    print(c)
    c.poner_caramelos(5)
    print(c)

    try:
        c.sacar_caramelos(30)
    except ValueError as e:  # Creo una variable e con el texto de la excepción
        print(f"No se pudo realizar la operación: {e}")
    else:
        print("Se pudo realizar la operación.")

    if len(c) > 30:
        c.sacar_caramelos(30)
        print("Se pudo realizar la operación.")
    else:
        print("No se pudo realizar la operación.")
    print(c)


main()
