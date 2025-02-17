from random import randint


def obtener_cantidad_dias_mes(mes, anio):
    dias = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # index 0   1   2   3   4   5   6   7   8   9   10  11  12
    cantidad = dias[mes]
    if mes == 2 and anio % 4 == 0:
        cantidad = 29
    return cantidad


def generar_fecha_random(anio):
    mes = randint(1, 12)
    dia = randint(1, obtener_cantidad_dias_mes(mes, anio))


'''
AAAAMM --> DD
def eld(aaaammdd):
    return aaaammdd % 100

AAAA --> MM <-- DD
def elm(aaaammdd):
    return (aaaammdd // 100) % 100

AAAA <-- MMDD
def ela(aaaammdd):
    return aaaammdd // 10000
'''


def eld(aaaammdd):
    return aaaammdd % 100


def elm(aaaammdd):
    return (aaaammdd // 100) % 100


def ela(aaaammdd):
    return aaaammdd // 10000


def fecha_str(aaaammdd):
    return f'{eld(aaaammdd):02}/{elm(aaaammdd):02}/{ela(aaaammdd):04}'


def main():
    fecha = 19630101  # AAAAMMDD
    print(fecha_str(fecha))


main()
