SUELDO_FIJO = float(input('Ingrese sueldo del vendedor: '))
ventas_mes = float(input('Ingrese el monto total de ventas en el mes: '))

comision = 0.16 * ventas_mes

cobrar = SUELDO_FIJO + comision

print(f'El importe a cobrar por el vendedor es: ${cobrar:.2f} pesos.')
