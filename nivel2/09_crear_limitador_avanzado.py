"""
Ejercicio 9: Limitador de Tasa Inteligente (Rate Limiter con Reset)
crear_limitador_avanzado(max_intentos, fn_alerta) cuenta ejecuciones
privadas y ejecuta fn_alerta cuando el limite se supera.
"""


def crear_limitador_avanzado(max_intentos, fn_alerta):
    if not isinstance(max_intentos, int) or isinstance(max_intentos, bool) or max_intentos < 1:
        raise ValueError("max_intentos debe ser un entero positivo")
    intentos = 0

    def ejecutar():
        nonlocal intentos
        intentos += 1
        if intentos > max_intentos:
            fn_alerta(intentos)
            return False
        return True

    def reset():
        nonlocal intentos
        intentos = 0

    ejecutar.reset = reset
    return ejecutar


if __name__ == "__main__":
    alerta = lambda n: print(f"ALERTA: limite excedido en intento {n}")
    limitador = crear_limitador_avanzado(2, alerta)

    print(limitador())
    print(limitador())
    print(limitador())
    limitador.reset()
    print(limitador())
