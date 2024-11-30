a = 10
b = 20
c = 30

# Una técnica (y por cada número agregamos otro if):
mayor = a

if b > mayor:
    mayor = b

if c > mayor:
    mayor = c

print(mayor)

# Otra forma:
mayor = max(a, b, c)
print(mayor)
