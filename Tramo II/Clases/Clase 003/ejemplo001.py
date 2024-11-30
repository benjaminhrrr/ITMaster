# A veces no coincide qué es lo que yo quiero que haga el algoritmo junto con
# lo que yo espero que haga.

a = 1
b = 3
c = 7

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > a:
        if b > c:
            print(b)
        else:
            print(c)
