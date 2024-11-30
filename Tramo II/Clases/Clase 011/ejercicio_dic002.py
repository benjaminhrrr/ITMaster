"""
Crear un diccionario donde las llaves sean las diferentes categorías de
productos ("ref" para refrigerados, "lim" para limpieza, "per" para productos
personales), y los valores sean listas de los nombres de los productos en esa
categoría.
Ejemplo:
    ("2002", "Huevos", 2.50, "ref"),
    ("2003", "Pan", 1.00, "alm"),
{"ref":["Huevos", "Carne",..., etc.], "alm": ["Pan", "Fideos",..., etc.]}
"""
from sys import path

path.insert(0, "Recursos/")
from datos import ARTICULOS_ALMACEN


def crear_dic(lista_productos: list) -> dict:
    dic_cat = {}
    for _, nombre, _, ref in lista_productos:
        if ref in dic_cat.keys():
            dic_cat[ref].append(nombre)
        else:
            dic_cat[ref] = [nombre]
    return dic_cat


def precio_promedio_por_ref(lista_productos: list) -> dict:
    dic = {}
    for _, _, precio, ref in lista_productos:
        if ref in dic.keys():
            dic[ref]["suma"] += precio
            dic[ref]["cont"] += 1
        else:
            dic[ref] = {"suma": precio, "cont": 1}
    for ref, dic_info in dic.items():
        dic[ref] = dic_info["suma"] / dic_info["cont"]
    return dic


def main():
    lista_productos = ARTICULOS_ALMACEN[:]
    print(crear_dic(lista_productos))
    for ref, precio in precio_promedio_por_ref(lista_productos).items():
        print(f"{ref:5} ${precio:8.2f}")


main()
