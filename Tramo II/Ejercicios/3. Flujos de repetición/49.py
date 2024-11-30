while True:
    opcion = input('¿Deseas continuar? [S/N]: ').strip().upper()
    if opcion == 'S':
        print('Continuando...')
        break
    elif opcion == 'N':
        print('Finalizando programa.')
        break
    else:
        print('Opción inválida. Por favor, ingresa S o N.')
