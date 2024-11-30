monto = int(input('Ingrese la cantidad de dinero a convertir: '))

billetes_mil = monto // 1000
monto %= 1000
billetes_doscientos = monto // 200
monto %= 200
billetes_cien = monto // 100
monto %= 100
billetes_cincuenta = monto // 50
monto %= 50
billetes_diez = monto // 10
monto %= 10
billetes_cinco = monto // 5
monto %= 5
billetes_uno = monto // 1

print(f'''Para la cantidad de {monto} se necesitan:
{billetes_mil} billetes de 1000.
{billetes_doscientos} billetes de 200.
{billetes_cien} billetes de 100.
{billetes_cincuenta} billetes de 50.
{billetes_diez} billetes de 10.
{billetes_cinco} billetes de 5.
{billetes_uno} billetes de 1.''')
