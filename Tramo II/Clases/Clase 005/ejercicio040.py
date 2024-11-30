'''
Escribir un programa que permita ingresar dos números enteros a y b con a <= b.
El programa debe mostrar:
    La suma de los números pares entre a y b.
    El producto de los números impares entre a y b.
'''

a = int(input('Ingrese a: '))
b = int(input('Ingrese b: '))

while b < a:
    print(f'Error: {b} < {a}')
    b = int(input('Ingrese b: '))

# Puedo usar ciclos para validar situaciones.

suma_pares = 0
producto_impares = 1

for numero in range(a, b+1):
    if numero % 2 == 0:
        suma_pares += numero
    else:
        producto_impares *= numero

print(f'''
Producto de los impares: {producto_impares}
Suma de los pares: {suma_pares}''')
