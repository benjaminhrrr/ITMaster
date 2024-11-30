guests = int(input('Cantidad de invitados: '))
seats = int(input('Cantidad de asientos disponibles: '))

if guests == seats:
    print('Alcanzan asientos.')
elif guests < seats:
    print('Sobran asientos.')
else:
    seats_needed = guests - seats
    print(f'Faltan {seats_needed} asientos.')
