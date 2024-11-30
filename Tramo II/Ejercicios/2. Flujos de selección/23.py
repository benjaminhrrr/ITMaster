n1 = int(input('Ingrese el primer número: '))
n2 = int(input('Ingrese el segundo número: '))
n3 = int(input('Ingrese el tercer número: '))

if n1 > n2 and n1 > n3:
    mayor = n1
elif n2 > n1 and n2 > n3:
    mayor = n2
else:
    mayor = n3

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3

if n1 != mayor and n1 != menor:
    medio = n1
elif n2 != mayor and n2 != menor:
    medio = n2
else:
    medio = n3

print(f'''
{menor} es el menor.
{medio} es el medio.
{mayor} es el mayor.''')
