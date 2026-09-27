"""
Ejercicio 11: Pipeline de Mapeo y Filtrado Combinado
La HOF procesar_coleccion(lista, fn_predicado, fn_transformacion)
combina internamente filter y map pasando expresiones lambda.
"""


def procesar_coleccion(lista, fn_predicado, fn_transformacion):
    return list(map(fn_transformacion, filter(fn_predicado, lista)))


if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(procesar_coleccion(numeros, lambda n: n % 2 == 0, lambda n: n ** 2))
    print(procesar_coleccion(numeros, lambda n: n > 5, lambda n: n * 10))
