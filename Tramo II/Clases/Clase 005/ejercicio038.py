'''
Escribir un programa que permita ingresar un número entero n. Debe mostrar los
primeros diez múltiplos de n.
'''

tabla = int(input('Número: '))

for n in range(1, 11):
    print(f'{tabla} x {n} = {tabla * n}')

print('n: ', n)
