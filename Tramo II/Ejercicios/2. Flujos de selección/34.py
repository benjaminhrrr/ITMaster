SUELDO_BASICO = float(input('Sueldo básico: '))
antiguedad = int(input('Antigüedad: '))
estado_civil = input('Estado civil: ').capitalize()

estados_civiles = ['Soltero', 'Casado']

des_jub = (11 * SUELDO_BASICO) / 100
des_os = (3 * SUELDO_BASICO) / 100
des_sin = (3 * SUELDO_BASICO) / 100

if estado_civil == estados_civiles[0]:
    incremento_soltero = (5 * SUELDO_BASICO) / 100
    sueldo_incrementado = SUELDO_BASICO + (incremento_soltero * antiguedad)
    sueldo_neto = sueldo_incrementado - des_jub - des_os - des_sin
elif estado_civil == estados_civiles[1]:
    incremento_casado = (7 * SUELDO_BASICO) / 100
    sueldo_incrementado = SUELDO_BASICO + (incremento_casado * antiguedad)
    sueldo_neto = sueldo_incrementado - des_jub - des_os - des_sin

sueldo_basico = '${:12,.2f}'.format(SUELDO_BASICO)
des_jub = '${:12,.2f}'.format(des_jub)
des_os = '${:12,.2f}'.format(des_os)
des_sin = '${:12,.2f}'.format(des_sin)
sueldo_neto = '${:12,.2f}'.format(sueldo_neto)

informe = f'''
-----------------------------
Estado civil:         {estado_civil}
Sueldo básico:  {sueldo_basico}
Antigüedad: {antiguedad:12,.0f} años
-----------------------------
DESCUENTOS:

Jubilación:     {des_jub}
Obra social:    {des_os}
Sindicato:      {des_sin}
-----------------------------
Sueldo neto:    {sueldo_neto}
-----------------------------
'''

print(informe)
