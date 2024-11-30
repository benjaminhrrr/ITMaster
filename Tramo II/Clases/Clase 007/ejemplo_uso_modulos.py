import sys

sys.path.append("Recursos/")
import funciones as fun


def main():
    x = fun.leer_entero("Número: ")


main()


"""
Cuando uno importa un módulo en otro módulo, si el módulo importado tiene
algo para ejecutar, ejecutará todo lo que pueda antes de iniciar a ejecutar el
módulo principal. Esto es porque python asignará el nombre "__main__" a todo
módulo que se ejecuta. Es por esto que cuando importamos un módulo, debemos
asegurarnos de que dicho módulo importado tenga un seguro que haga que sólo
ejecute lo que pueda ejecutar si lo ejecutamos con nombre de módulo principal.

* Es por esto que para el módulo "funciones" agregamos un condicional a la
función "test_funciones()" que sólo se ejecutará si inicializamos dicho módulo
como módulo principal.
"""
