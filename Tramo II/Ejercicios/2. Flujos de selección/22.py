n1 = int(input('Ingrese un número: '))
n2 = int(input('Ingrese otro número: '))
n3 = int(input('Ingrese otro número: '))

if n1 > n2 and n1 > n3:
    mayor = n1
elif n2 > n1 and n2 > n3:
    mayor = n2
else:
    mayor = n3

print(f'{mayor} es el mayor.')
