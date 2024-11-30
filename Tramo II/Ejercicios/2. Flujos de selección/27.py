name = input('Nombre: ')

while True:
    age = int(input('Edad (entre 1 y 120 años): '))
    gender = input('Género (M o F): ').upper()
    if 1 <= age <= 120 and gender in ['M', 'F']:
        break
    elif (age < 1 or age > 120) and gender not in ['M', 'F']:
        print('Datos inválidos. Intente nuevamente.')
    else:
        if age < 1 or age > 120:
            print('Edad fuera de rango. Intente nuevamente.')
        elif gender not in ['M', 'F']:
            print('Género inválido. Intente nuevamente.')

if (age >= 65) and (gender == 'M') or (age >= 60) and (gender == 'F'):
    print(f'{name} está en edad de jubilarse')
else:
    print(f'{name} no está en edad de jubilarse')
