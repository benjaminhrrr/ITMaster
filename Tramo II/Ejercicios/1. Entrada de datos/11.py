socios = {}

for i in range(3):
    nombre = input(f'Ingrese el nombre del socio {i+1}: ')
    capital = float(input(f'Ingrese el capital aportado por {nombre}: '))
    socios[nombre] = capital

total_aportado = sum(socios.values())

print(f'''\nEl valor total aportado a la sociedad es: ${total_aportado:.2f}
\nPorcentaje de aportación de cada socio:''')

for nombre, capital in socios.items():
    porcentaje = (capital / total_aportado) * 100
    print(f'{nombre}: {porcentaje:.2f}%')
