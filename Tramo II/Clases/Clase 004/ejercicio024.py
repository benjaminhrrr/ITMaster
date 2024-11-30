'''
Escribir un programa en Python que solicite al usuario su edad y estatura, y
que determine si cumple con los requisitos para subir a la atracción. Si
cumple con ambos requisitos, el programa debe imprimir "¡Puede acceder!" en la
pantalla. Si no cumple con alguno de los requisitos, el programa debe imprimir
un mensaje que indique el motivo por el cual no puede subir. Por ejemplo, si
no cumple con el requisito de la edad, el programa debe imprimir "Lo siento,
eres demasiado joven para acceder". Si no cumple con el requisito de la
estatura, el programa debe imprimir "Lo siento, eres demasiado bajo para
acceder".
'''

nombre = input('Nombre: ')
edad = int(input('Edad: '))
altura = float(input('Altura: '))

LIMITE_EDAD = 10
LIMITE_ALTURA = 1.60

entra_edad = edad >= LIMITE_EDAD
entra_altura = altura > LIMITE_ALTURA
entra = entra_edad and entra_altura

if entra:
    cartel = 'Entraste'
else:
    cartel = 'No entras'
    if not entra_altura:
        cartel += ' altura'
    if not entra_edad:
        cartel += ' edad'

print(f'{nombre} {cartel}')

# Está bien de la forma en la que yo lo hice pero no es una buena práctica
# pues el código resulta ser menos legible y difícil de trabajar.
