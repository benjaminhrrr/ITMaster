'''
Escribir un programa que a partir de un número entero cant ingresado por el
usuario permita cargar por teclado cant número enteros. La computadora debe
mostrar cuál fue el mayor número y en qué posición apareció.

En computación un número random es un número que está entre 0.0 ... 0.9999
'''

from random import randint

cant = randint(1, 10)
maximo = -float('inf')
posicion = 0

for x in range(cant):
    numero = randint(-1000, 1000)
    print(f'{x + 1}. {numero}')
    if numero > maximo:
        maximo = numero
        posicion = x + 1

print(f'Cantidad de números: {cant}')
print(f'Máximo: {maximo}')
print(f'Posición: {posicion}')
