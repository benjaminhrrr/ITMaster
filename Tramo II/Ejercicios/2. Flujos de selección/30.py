n1 = int(input('Número: '))
n2 = int(input('Número: '))

if n2 <= n1:
    mayor = n1
    menor = n2
else:
    mayor = n2
    menor = n1

if mayor % menor == 0:
    print(f'{mayor} es divisible por {menor}')
else:
    print(f'{mayor} no es divisible por {menor}')
