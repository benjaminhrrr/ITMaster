from sys import path

path.insert(0, "Recursos/")
from datos import ARTICULOS_ALMACEN


def filtrar(articulos: list, filtro: str) -> list:
    lista_salida = []
    # (codigo, nombre, precio, categoria)
    for codigo, nombre, precio, categoria in articulos:
        print(codigo, nombre, precio, categoria)
        if filtro == categoria:
            lista_salida.append([codigo, nombre, precio])
    return lista_salida


def orden_codigo(dato: tuple) -> str:
    return dato[0]


def orden_nombre(dato: tuple) -> str:
    return dato[1]


def orden_precio(dato: tuple) -> float:
    return dato[2]


def orden_categoria(dato: tuple) -> str:
    return dato[3]


def main():
    articulos = ARTICULOS_ALMACEN[:]
    alm = filtrar(articulos, "ref")
    alm.sort(key=orden_precio, reverse=True)
    for codigo, nombre, precio in alm:
        print(f"{codigo:10} {nombre[:30]:30} {precio:10.2f}")


main()
