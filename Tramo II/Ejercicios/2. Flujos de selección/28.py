month_number = int(input('Número de mes: ')) - 1

months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
          'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

while True:
    month = input('Mes: ').capitalize()
    if month == months[month_number]:
        print('Válido.')
        break
    else:
        print('Inválido')
