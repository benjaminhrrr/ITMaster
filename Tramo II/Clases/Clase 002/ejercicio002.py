'''
En python hay diferentes tipos de datos básicos:

(int) enteros
(float) números de punto flotante
(bool) V o F
(str) cadenas de caracteres: 'Hola mundo'
(NoneType) ausencia de valor
(bytes y bytesarray) datos binarios
(range) secuencia inmutable de números comunmente utilizada en bucles for

(list) colección de elementos ordenados y modificables:
    list = [1, 2, 3]

(tuple) colección de elementos ordenados e inmutables:
    tuple = (1, 2, 3)

(set) colección de elementos únicos y no ordenados:
    set = {1, 2, 3}

(dict) colección de pares clave-valor:
    dictionary = {'name': ' Ben', 'age': 24}

También es posible la cración de datos propios definidos por el usuario
utilizando clases.

Es importante tener en cuenta que python es de tipado dinámico, lo que
significa que no es necesario declarar explícitamtne el tipo de una variable;
python lo infiere según el valor asignado a la variable. Esto hace que sea
flexible y fácil de utilizar prestando atención a los tipos de datos para
evitar errores de tipo.
'''

print(123.4, type(123.4))
a = 2
b = 3.5
c = '125'
x = a > b
n = 'qqq'
print('a:', a, 'Tipo de a:', type(a))
print('b:', b, 'Tipo de b:', type(b))
print('c:', c, 'Tipo de c:', type(c))
print('x:', x, 'Tipo de x:', type(x))
print('n:', n, 'Tipo de n:', type(n))
print(type(None))
