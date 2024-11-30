n1 = int(input('Número: '))
n2 = int(input('Número: '))

operacion = input('Operación (+, -, *, /): ')

if operacion == '+':
    resultado = n1 + n2
elif operacion == '-':
    resultado = n1 - n2
elif operacion == '*':
    resultado = n1 * n2
elif operacion == '/':
    if n2 == 0:
        resultado = 'ERROR'
    else:
        resultado = n1 / n2
else:
    resultado = 'Operación no válida'

print(f'{resultado}')
