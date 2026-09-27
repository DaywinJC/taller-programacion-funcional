"""
Ejercicio 12: Reductor / Agrupador Personalizado
La HOF agrupar_por(lista, fn_clave) recibe una coleccion de
diccionarios y los agrupa en un diccionario clave-valor basandose en el
resultado de la lambda fn_clave.
"""


def agrupar_por(lista, fn_clave):
    resultado = {}
    for elemento in lista:
        clave = fn_clave(elemento)
        resultado.setdefault(clave, []).append(elemento)
    return resultado


if __name__ == "__main__":
    estudiantes = [
        {"nombre": "Ana", "curso": "A"},
        {"nombre": "Luis", "curso": "B"},
        {"nombre": "Marta", "curso": "A"},
        {"nombre": "Juan", "curso": "C"},
    ]

    print(agrupar_por(estudiantes, lambda e: e["curso"]))

    numeros = [1, 2, 3, 4, 5, 6, 7, 8]
    print(agrupar_por(numeros, lambda n: "par" if n % 2 == 0 else "impar"))
