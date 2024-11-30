while True:
    n1 = float(input('Nota Nº1: '))
    n2 = float(input('Nota Nº2: '))
    if 1 <= n1 <= 10 and 1 <= n2 <= 10:
        if n1 >= 7 and n2 >= 7:
            print('Promociona')
        elif n1 >= 4 and n2 >= 4:
            print('Aprueba')
        else:
            print('Recupera')
        break
    else:
        print('Error. Notas fuera de rango.')
