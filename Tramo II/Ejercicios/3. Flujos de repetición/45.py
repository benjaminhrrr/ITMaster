p = 1

while True:
    try:
        a = int(input('Ingrese un primer número natural: '))
        b = int(input('Ingrese un segundo número natural: '))
        if a <= 0 or b <= 0:
            print('ERROR. Ambos números deben ser naturales.')
        elif 0 < a and 0 < b:
            for i in range(b):
                p *= a
            break
    except ValueError:
        print('Datos inválidos. Intente nuevamente.')

p_format = f'{a} ^ {b} = {p} = ' + ' x '.join([str(a) for _ in range(b)])

print(p_format)
