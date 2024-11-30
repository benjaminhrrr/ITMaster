'''
Leer un grupo de diez datos. Mostrar la suma.
'''

suma = 0

for n in range(10):
    numero = int(input('Número: '))
    suma += numero

print(f'Suma: {suma}')
