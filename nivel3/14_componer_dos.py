"""
Ejercicio 14: Compositor de Cadenas de Operaciones
Crea la HOF componer_dos(f, g) que devuelva un closure que aplique
f(g(x)), permitiendo encadenar transformaciones complejas en linea.
"""


def componer_dos(f, g):
    def compuesta(x):
        return f(g(x))
    return compuesta


if __name__ == "__main__":
    incrementar = lambda x: x + 1
    duplicar = lambda x: x * 2

    incrementar_luego_duplicar = componer_dos(duplicar, incrementar)
    duplicar_luego_incrementar = componer_dos(incrementar, duplicar)

    print(incrementar_luego_duplicar(5))  # (5+1)*2 = 12
    print(duplicar_luego_incrementar(5))  # (5*2)+1 = 11

    mayusculas_e_invertido = componer_dos(lambda t: t[::-1], lambda t: t.upper())
    print(mayusculas_e_invertido("python"))
