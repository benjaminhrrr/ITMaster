ancho_terreno = float(input('Ingrese el ancho del terreno en metros: '))
largo_terreno = float(input('Ingrese el largo del terreno en metros: '))

valor_m2 = float(input('Ingrese el valor del metro cuadrado de tierra: '))

area_terreno = ancho_terreno * largo_terreno

valor_total_terreno = area_terreno * valor_m2

perimetro_1 = 2 * (ancho_terreno + largo_terreno)
perimetro_2 = (2 * (ancho_terreno + largo_terreno)) * 2
perimetro_3 = (2 * (ancho_terreno + largo_terreno)) * 3

print(f'''\nEl valor total del terreno es: ${valor_total_terreno:.2f} pesos.
\nMetros de alambre necesarios para cercar a tres alturas distintas:
A un metro de altura: {perimetro_1}m.
A dos metros de altura: {perimetro_2}m.
A tres metros de altura: {perimetro_3}m.''')
