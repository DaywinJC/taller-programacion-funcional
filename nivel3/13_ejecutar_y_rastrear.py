"""
Ejercicio 13: Ejecutor Repetitivo con Estado Accesible
Crea la HOF ejecutar_y_rastrear(fn_tarea, n) que retorne un closure con
el historial de resultados de haber ejecutado fn_tarea N veces.
"""


def ejecutar_y_rastrear(fn_tarea, n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n debe ser un entero no negativo")
    historial = []

    def ejecutar_todo(*args, **kwargs):
        for _ in range(n):
            historial.append(fn_tarea(*args, **kwargs))
        return list(historial)

    def obtener_historial():
        return list(historial)

    ejecutar_todo.historial = obtener_historial
    return ejecutar_todo


if __name__ == "__main__":
    import random
    random.seed(1)

    lanzar_dado = ejecutar_y_rastrear(lambda: random.randint(1, 6), 5)
    print(lanzar_dado())
    print(lanzar_dado.historial())

    contador_llamadas = ejecutar_y_rastrear(lambda x: x * 2, 3)
    print(contador_llamadas(4))
