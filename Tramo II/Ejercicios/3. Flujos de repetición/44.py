s = 0

while True:
    try:
        a = int(input('Ingrese un primer número entero positivo: '))
        b = int(input('Ingrese un segundo número entero positivo: '))
        if a <= 0 or b <= 0:
            print('ERROR. Ambos números deben ser enteros positivos.')
        elif 0 < a and 0 < b:
            for i in range(b):
                s += a
            break
    except ValueError:
        print('Datos inválidos. Intente nuevamente.')

s_format = f'{a} x {b} = {s} = ' + ' + '.join([str(a) for _ in range(b)])

print(s_format)
