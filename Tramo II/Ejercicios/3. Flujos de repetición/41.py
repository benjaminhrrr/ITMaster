max = None

while True:
    try:
        num = int(input('Ingrese un número entero: '))
        if num == 0:
            break
        if max is None or max < num:
            max = num
    except ValueError:
        print('Error: dato inválido.')

if max is not None:
    print(f'El máximo es: {max}')
else:
    print('No se ingresó ningún dato.')
