"""
Ejercicio 1: Generador de Formateadores con Transformación
crear_formateador(prefijo, fn_transformacion) devuelve un closure que
procesa un texto aplicando la lambda/función fn_transformacion y
concatena el prefijo.
"""


def crear_formateador(prefijo, fn_transformacion):
    def formatear(texto):
        return prefijo + fn_transformacion(texto)
    return formatear


if __name__ == "__main__":
    formateador_mayus = crear_formateador("[LOG] ", lambda t: t.upper())
    formateador_invertido = crear_formateador(">> ", lambda t: t[::-1])

    print(formateador_mayus("sistema iniciado"))
    print(formateador_invertido("python"))
    print(crear_formateador("Usuario: ", lambda t: t.strip().title())("  ana lopez  "))
