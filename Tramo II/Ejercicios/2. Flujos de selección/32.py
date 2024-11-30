km = float(input('Cantidad de km: '))
VIAJE_MINIMO = 50
TARIFA_1 = 20
TARIFA_2 = 15

if 0 < km < 10:
    precio = (km * TARIFA_1) + VIAJE_MINIMO
    print(f'El precio es: ${precio} pesos.')
elif 10 <= km:
    precio = (km * TARIFA_2) + VIAJE_MINIMO
    print(f'El precio es: ${precio} pesos.')
