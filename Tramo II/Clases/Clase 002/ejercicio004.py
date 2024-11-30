'''
Leer tres numeros.
    Leer un numero.
    Leer un numero.
    Leer un numero.
Calcular promedio.
Mostrar resultado.
'''

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))
avg = (n1 + n2 + n3) / 3

print('Notas:', n1, n2, n3, 'Promedio:', avg)

cadena_formato = f'Notas: [{n1},{n2},{n3}] --> Promedio: {avg}'
print(cadena_formato)
