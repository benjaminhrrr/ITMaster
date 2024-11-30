def calculo_salario(nombre, salario_base, ventas, valor_v):
    comision_fija = 100
    comision = 0.05 * valor_v
    salario_total = salario_base + (comision_fija * ventas) + comision
    return nombre, salario_total


vendedor = input('Ingrese el nombre del vendedor: ')
salario_base = float(input('Ingrese el salario base del vendedor: '))
ventas = int(input('Ingrese la cantidad de ventas realizadas: '))
valor_v = float(input('Ingrese el valor total de las ventas realizadas: '))

nombre, salario = calculo_salario(vendedor, salario_base, ventas, valor_v)

print(f'El salario de {nombre} en este mes es: ${salario}.')
