"""
Ejercicio 15: Decorador / HOF de Profiling y Auditoria
Crea la HOF auditar_ejecucion(fn_objetivo, fn_logger) que mida el
tiempo y envie el informe de ejecucion al closure/lambda de logging
pasado por parametro.
"""

import time


def auditar_ejecucion(fn_objetivo, fn_logger):
    def envoltura(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = fn_objetivo(*args, **kwargs)
        duracion = time.perf_counter() - inicio
        fn_logger(fn_objetivo.__name__, duracion, resultado)
        return resultado
    return envoltura


if __name__ == "__main__":
    logger_simple = lambda nombre, dur, res: print(
        f"[AUDITORIA] {nombre} -> resultado={res} tiempo={dur:.6f}s"
    )

    def tarea_pesada(n):
        return sum(i * i for i in range(n))

    tarea_auditada = auditar_ejecucion(tarea_pesada, logger_simple)
    print(tarea_auditada(100000))
