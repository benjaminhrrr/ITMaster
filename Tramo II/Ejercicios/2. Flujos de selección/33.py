importe = float(input('Importe de la compra: '))
DESCUENTO_1 = 4.5
DESCUENTO_2 = 8
DESCUENTO_3 = 10.5

if importe <= 5500:
    descuento = (importe * DESCUENTO_1) / 100
    importe_final = importe - descuento
    print(f'Descuento: ${descuento}\nImporte: ${importe_final}')
elif 5500 < importe <= 10000:
    descuento = (importe * DESCUENTO_2) / 100
    importe_final = importe - descuento
    print(f'Descuento: ${descuento}\nImporte: ${importe_final}')
else:
    descuento = (importe * DESCUENTO_3) / 100
    importe_final = importe - descuento
    print(f'Descuento: ${descuento}\nImporte: ${importe_final}')
