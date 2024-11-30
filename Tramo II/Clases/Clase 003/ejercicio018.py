'''
Escribir un programa que permita al usuario ingresar un número entero y luego
muestre un mensaje indicando si el número es par o impar.

Pensando los pasos para resolver el problema:
1. Pedir al usuario que ingrese un número entero.
2. Almacenar ese número en una variable.
3. Verificar si el número es par o impar.

Si el número es par, mostrar un mensaje indicando que es par.
Si el número es impar, mostrar un mensaje indicando que es impar.

# División entera
a // 1

# Resto de la división
c % 1
'''

variable = int(input('Número: '))
es_par = (variable % 2) == 0

if es_par:
    print('Es par', type(variable))
else:
    print('Es impar', type(variable))

if (variable % 2) == 0:
    print('Es par', type(variable))
else:
    print('Es impar', type(variable))

print(es_par, type(es_par))
