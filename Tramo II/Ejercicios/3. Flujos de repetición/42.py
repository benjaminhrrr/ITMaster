sum = 0
counter = 0

while True:
    num = int(input('Ingrese un número entero: '))
    if num == 0:
        break
    sum += num
    counter += 1

if counter == 0:
    avg = 0
else:
    avg = sum / counter

print(f'El promedio de los números ingresados es: {avg}')
