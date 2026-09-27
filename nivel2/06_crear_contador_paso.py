"""
Ejercicio 6: Contador Ponderado
crear_contador_paso(fn_paso) incrementa su estado interno utilizando
una lambda fn_paso(cuenta_actual) en lugar de un incremento fijo.
"""


def crear_contador_paso(fn_paso):
    cuenta = 0

    def siguiente():
        nonlocal cuenta
        cuenta = fn_paso(cuenta)
        return cuenta
    return siguiente


if __name__ == "__main__":
    contador_doble = crear_contador_paso(lambda actual: actual * 2 + 1)
    contador_de_tres = crear_contador_paso(lambda actual: actual + 3)

    print(contador_doble())
    print(contador_doble())
    print(contador_doble())
    print(contador_de_tres())
    print(contador_de_tres())
