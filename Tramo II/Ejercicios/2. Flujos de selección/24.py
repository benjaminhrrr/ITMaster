age = int(input('Ingrese su edad: '))
height = float(input('Ingrese su estatura en metros: '))

if (age >= 10) and (height >= 1.60):
    print('¡Puede acceder!')
elif (age < 10) and (height < 1.60):
    print('No puede acceder.')
elif (age < 10) or (height < 1.60):
    if age < 10:
        print('Lo siento, eres demasiado joven para acceder.')
    else:
        print('Lo siento, eres demasiado bajo para acceder.')
