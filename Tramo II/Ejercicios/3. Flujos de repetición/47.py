while True:
    try:
        nota = float(input('Ingrese la nota del examen (0-10): '))
        if 0 <= nota <= 10:
            print('Válida')
            break
        else:
            print('La nota debe estar entre 0 y 10. Intente nuevamente.')
    except ValueError:
        print('Ingrese un dato válido.')
