"""
Este Módulo implementa funciones de uso general.

- titulo(cadena: str) -> str
- menu(str_opciones: str) -> int
- es_entero(str_numero: str) -> bool
- es_flotante(str_numero: str) -> bool
- es_numero(str_numero: str) -> bool
- leer_entero_entre(cartel_para_el_usuario, desde, hasta) -> int
- leer_flotante_entre(cartel_para_el_usuario, desde, hasta) -> float
- leer_numero(cartel: str = "Ingrese un número: ") -> int | float
"""


def titulo(cadena: str) -> str:
    return f"{'-'*82}\n{cadena.upper().center(82)}\n{'-'*82}"


def menu(str_opciones: str) -> int:
    lista_opciones = str_opciones.replace("\n", "").split(",")
    for index, cadena in enumerate(lista_opciones):
        if index == 0:
            print(titulo(cadena))
        else:
            print(f"{index} - {cadena}")
    return leer_entero("Ingrese una opción: ", 1, index)


def es_entero(str_numero: str) -> bool:
    try:
        int(str_numero)
    except:  # SI HAY ERROR
        return False
    else:  # SI NO HAY ERROR
        return True


def es_flotante(str_numero: str) -> bool:
    try:
        float(str_numero)
    except:  # SI HAY ERROR
        return False
    else:  # SI NO HAY ERROR
        return True


def es_numero(str_numero: str) -> bool:
    return es_entero(str_numero) or es_flotante(str_numero)


def leer_entero(
    cartel: str = "Ingrese un entero: ",
    desde: int = -9999999999999,
    hasta: int = 9999999999999,
) -> int:
    todo_ok = False
    while not todo_ok:  # Mientras error
        cadena = input(cartel)
        if es_entero(cadena):
            numero = int(cadena)
            if desde <= numero <= hasta:
                todo_ok = True
            else:
                print(f"Error: número fuera del rango [{desde}...{hasta}].")
        else:
            print("Error: tiene que ingresar un número entero.")
    return numero


def leer_flotante(
    cartel: str = "Ingrese un float: ",
    desde: float = -float("inf"),
    hasta: float = float("inf"),
) -> float:
    todo_ok = False
    while not todo_ok:  # Mientras error
        cadena = input(cartel)
        if es_flotante(cadena):
            numero = float(cadena)
            if desde <= numero <= hasta:
                todo_ok = True
            else:
                print(f"Error: número fuera del rango [{desde}...{hasta}].")
        else:
            print("Error: tiene que ingresar un número float.")
    return numero


def leer_numero(cartel: str = "Ingrese un número: ") -> int | float:
    while True:
        cadena = input(cartel)
        if es_entero(cadena):
            return int(cadena)
        elif es_flotante(cadena):
            return float(cadena)
        else:
            print("Error: tiene que ingresar un número.")


def test_funciones():
    print(leer_numero("Importe: "))
    print(leer_numero("Edad: "))
    print(f"El nombre es: {__name__}")
    print(leer_entero())
    print(leer_entero("Ingrese un número: "))
    print(leer_entero(desde=0))
    print(leer_entero("Día: ", 1, 31))
    print(leer_entero(hasta=10, cartel="Holi: ", desde=1))


# *
if __name__ == "__main__":
    test_funciones()
