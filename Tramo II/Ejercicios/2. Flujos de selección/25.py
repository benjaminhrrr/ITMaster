age = int(input('Ingrese su edad: '))
height = float(input('Ingrese su estatura en metros: '))

if (age > 6) or (height > 1.50):
    print('¡Puede acceder!')
elif (age <= 6) and (height <= 1.50):
    print('No puede acceder.')
