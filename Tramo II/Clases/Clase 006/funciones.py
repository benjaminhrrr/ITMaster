# Las funciones deben tener un solo objetivo (hacer una sola cosa).
# Su nombre y sus parámetros deben ser consistentes con su objetivo.


def leer_entero(cartel_para_el_usuario):
    todo_ok = False
    while not todo_ok:  # Mientras error
        cadena = input(cartel_para_el_usuario)
        if cadena.isnumeric():
            todo_ok = True
        else:
            print('Error: tiene que ingresar un número entero.')
    numero = int(cadena)
    return numero


def leer_entero_entre(cartel_para_el_usuario, desde, hasta):
    todo_ok = False
    while not todo_ok:  # Mientras error
        cadena = input(cartel_para_el_usuario)
        if cadena.isnumeric():
            numero = int(cadena)
            if desde <= numero <= hasta:
                todo_ok = True
            else:
                print(f'Error: número fuera del rango [{desde}...{hasta}].')
        else:
            print('Error: tiene que ingresar un número entero.')
    return numero


a = 10  # Variable global (no nos gusta)
# Preferimos variables locales, las que están dentro de las funciones.


def test_funciones():
    cantidad_patas = leer_entero_entre('Ingrese la cantidad de patas: ', 1, 4)
    dia = leer_entero_entre('Día: ', 1, 31)
    mes = leer_entero_entre('Mes: ', 1, 12)


test_funciones()
