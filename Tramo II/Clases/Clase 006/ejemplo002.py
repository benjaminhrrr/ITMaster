'''
Leer un número y mostrar la cantidad de dígitos.
numero = 123456789 --> 9
'''


def contar_los_digitos(numero):
    cadena = str(numero)
    return len(cadena)


def test():
    numero = int(input('Ingrese un número: '))
    cantidad_digitos = contar_los_digitos(numero)
    print(f'Cantidad de dígitos: {cantidad_digitos}')


test()  # Programa principal

# Las funciones deben tener un solo objetivo. Son herramientas.
# Tengo que saber lo que quiero hacer.
