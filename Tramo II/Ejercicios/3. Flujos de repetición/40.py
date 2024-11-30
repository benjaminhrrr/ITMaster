a = int(input('Ingrese a: '))
b = int(input('Ingrese b: '))

suma_pares = 0
producto_impares = 1

for numero in range(a, b+1):
    if numero % 2 == 0:
        suma_pares += numero
    else:
        producto_impares *= numero

print(f'''
Producto de los impares entre {a} y {b}: {producto_impares}
Suma de los pares entre {a} y {b}: {suma_pares}''')
