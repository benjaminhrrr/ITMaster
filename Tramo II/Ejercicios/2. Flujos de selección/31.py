COSTO_BASICO = 1000
COSTO_POR_PAGINA = 35.10
COSTO_ENC_RUSTICA = 880
COSTO_ENC_ESPECIAL = 1200

n_pags = int(input('Ingrese número de páginas: '))
costo = COSTO_BASICO + (COSTO_POR_PAGINA * n_pags)

if 300 < n_pags <= 600:
    costo += COSTO_ENC_RUSTICA
elif 600 < n_pags:
    costo += COSTO_ENC_ESPECIAL

print(f'El costo del libro es: {costo}')
