'''
Existen dos reglas que identifican dos conjuntos de valores:
    a) El número es de un solo dígito.
    b) El número es impar.
A partir de estas reglas, escribir un programa que permita ingresar un número
entero.
Debe asignar el valor que corresponda a las variables booleanas:
    esDeUnSoloDigito
    esImpar
    estaEnAmbos
    noEstaEnNinguno
el valor V o F, según corresponda, para indicar si el valor número ingresado
pertenece o no a cada conjunto. Definir un lote de prueba de varios
números y probr el algoritmo, escribiendo los resultados.
'''

numero = int(input('Número: '))

esDeUnSoloDigito = -9 <= numero <= 9
esImpar = (numero % 2) != 0
estaEnAmbos = esDeUnSoloDigito and esImpar
noEstaEnNinguno = not esDeUnSoloDigito and not esImpar

print(f'''{numero}
esDeUnSoloDigito: {esDeUnSoloDigito}
esImpar: {esImpar}
estaEnAmbos: {estaEnAmbos}
noEstaEnNinguno: {noEstaEnNinguno}''')
