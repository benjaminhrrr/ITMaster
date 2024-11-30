a1 = float(input('Ingrese el valor en grados del primer ángulo interior: '))
a2 = float(input('Ingrese el valor en grados del segundo ángulo interior: '))

if 0 < a1 + a2 < 180:
    a_restante = 180 - (a1 + a2)
    print(f'El ángulo restante es: {a_restante}º')
else:
    print('''\nERROR: no es posible efectuar la operación.\n
Motivos posibles:
Ha ingresado valores menores que 0º.
Ha ingresado el valor de solamente un ángulo.
La suma total es mayor que 180º.''')
