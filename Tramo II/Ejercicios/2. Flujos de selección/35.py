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
