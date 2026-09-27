"""
Ejercicio 18: Motor de Pipeline Secuencial (Currying / Middleware)
Crea crear_pipeline(*funciones_transformacion) que permita pasar un
dato inicial y hacerlo fluir en orden a traves de todas las
lambdas/funciones del pipeline.
"""


def crear_pipeline(*funciones_transformacion):
    def ejecutar(dato_inicial):
        resultado = dato_inicial
        for funcion in funciones_transformacion:
            resultado = funcion(resultado)
        return resultado
    return ejecutar


if __name__ == "__main__":
    pipeline_texto = crear_pipeline(
        lambda t: t.strip(),
        lambda t: t.lower(),
        lambda t: t.replace(" ", "_"),
    )
    print(pipeline_texto("  Hola Mundo Python  "))

    pipeline_numeros = crear_pipeline(
        lambda n: n + 10,
        lambda n: n * 2,
        lambda n: n - 5,
    )
    print(pipeline_numeros(5))
