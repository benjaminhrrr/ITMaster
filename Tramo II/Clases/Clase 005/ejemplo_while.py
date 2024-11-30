'''
Leer un conjunto de números hasta que se ingrese un cero. Mostrar la suma.

conjunto1 --> 1,5,4,7,8,5,4,5,8,7,4,5,8,7,0
conjunto2 --> 4,5,8,7,4,5,8,7,0
conjunto3 --> 0

Mi algoritmo debería procesar cualquiera de estos conjuntos de datos sin
inconvenientes.
Este es un caso en el que sé cómo terminan los datos '0'. A este concepto se
lo conoce como centinela.

El esquema que vamos a utilizar es el esquema básico de lectura y se denomina
'lectura adelantada'.
'''

# Teorema fundamental de la programación estructurada: inicio-proceso-fin.

# ANTES (para todos)
suma = 0
numero = int(input('Número: '))
while numero != 0:
    # DURANTE (para cada dato)
    suma += numero  # suma = suma + numero (más o menos) ¡No nos gusta!
    numero = int(input('Número: '))
# DESPUÉS (totales)
print(f'Suma: {suma}')
