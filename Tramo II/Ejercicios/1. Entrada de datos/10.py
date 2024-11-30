investor_1 = float(input('Ingrese dinero invertido por la persona uno: '))
investor_2 = float(input('Ingrese dinero invertido por la persona dos: '))
investor_3 = float(input('Ingrese dinero invertido por la persona tres: '))

total = investor_1 + investor_2 + investor_3

percentage_i1 = round((investor_1 / total * 100), 2)
percentage_i2 = round((investor_2 / total * 100), 2)
percentage_i3 = round((investor_3 / total * 100), 2)

print(f'''\nPorcentaje de inversión por cada inversor:
Inversor 1: {percentage_i1}%
Inversor 2: {percentage_i2}%
Inversor 3: {percentage_i3}%''')
