"""
Ejercicio 7: Acumulador con Filtro de Aceptacion
crear_acumulador_validado(criterio_lambda) mantiene un total acumulado
privado, pero solo suma los valores que superen la prueba de la lambda
enviada.
"""


def crear_acumulador_validado(criterio_lambda):
    total = 0

    def acumular(valor):
        nonlocal total
        if criterio_lambda(valor):
            total += valor
        return total
    return acumular


if __name__ == "__main__":
    acumulador_positivos = crear_acumulador_validado(lambda v: v > 0)
    acumulador_pares = crear_acumulador_validado(lambda v: v % 2 == 0)

    print(acumulador_positivos(10))
    print(acumulador_positivos(-5))
    print(acumulador_positivos(20))
    print(acumulador_pares(3))
    print(acumulador_pares(4))
    print(acumulador_pares(8))
