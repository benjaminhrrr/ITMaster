'''
y = f(x)
y = x²
'''


def cuadrado(x):
    return x * x


def main():
    print('Hola función')
    resultado = cuadrado(5)
    print(f'Resultado: {resultado}')
    a = 10
    resultado = cuadrado(a)
    print(f'Resultado: {resultado}')
    resultado = cuadrado(cuadrado(2))
    print(f'Resultado: {resultado}')


main()  # Punto de entrada al programa (el programa empieza acá)

# 'main()' siempre al final
# No nos gusta definir funciones dentro de funciones
# No nos gusta lo global (variables globales)
# Hay que pensar dónde podría modularizar
