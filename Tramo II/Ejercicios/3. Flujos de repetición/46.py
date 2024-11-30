from random import randint

n = int(input('Ingrese un número entero: '))
cant = randint(1, n)
maximo = -float('inf')
posicion = 0

for i in range(cant):
    numero = randint(-1000, 1000)
    print(f'{i + 1}. {numero}')
    if numero > maximo:
        maximo = numero
        posicion = i + 1

print(f'Cantidad de números generados: {cant}')
print(f'Máximo: {maximo}')
print(f'Posición: {posicion}')
