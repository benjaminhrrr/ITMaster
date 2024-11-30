desde = 1
cant = 11
salto = 2

# Siempre que escribo range() se crea un objeto nuevo.
# Ese objeto es iterable.
# El for solo se utiliza para recorrer una lista iterable.

print(range(desde, cant, salto))
print(len(range(desde, cant, salto)))
print(list(range(desde, cant, salto)))

for n in range(desde, cant, salto):
    print(n, end=' ', sep=' - ')
