while True:
    operation = input('Operación (+, -, *, / o F): ').strip().upper()
    if operation == 'F':
        print('Programa finalizado.')
        break
    if operation in ('+', '-', '*', '/'):
        n1 = int(input('Número: '))
        n2 = int(input('Número: '))
        if operation == '+':
            result = n1 + n2
        elif operation == '-':
            result = n1 - n2
        elif operation == '*':
            result = n1 * n2
        elif operation == '/':
            if n2 == 0:
                print('No se puede dividir entre cero.')
                continue
            result = n1 / n2
        print(f'{n1} {operation} {n2} = {result}')
    else:
        print('Operación inválida. Ingrese +, -, *, / o F.')
