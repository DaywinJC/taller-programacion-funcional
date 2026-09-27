"""
Ejercicio 2: Multiplicador Parametrico con Mapeo
crear_operador(factor, operacion_lambda) devuelve un closure capaz de
aplicar la operacion recibida utilizando el factor encapsulado.
"""


def crear_operador(factor, operacion_lambda):
    def operar(valor):
        return operacion_lambda(valor, factor)
    return operar


if __name__ == "__main__":
    duplicar = crear_operador(2, lambda x, f: x * f)
    elevar = crear_operador(3, lambda x, f: x ** f)
    restar_factor = crear_operador(5, lambda x, f: x - f)

    print(duplicar(10))
    print(elevar(2))
    print(restar_factor(20))
    print([duplicar(v) for v in [1, 2, 3, 4]])
