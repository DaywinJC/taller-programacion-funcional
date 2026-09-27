"""
Ejercicio 3: Calculador de Descuentos con Regla Dinamica
crear_descuento_dinamico(regla_condicional_lambda) devuelve un closure
que evaluara el precio con la lambda enviada para determinar si aplica
un descuento prefijado.
"""


def crear_descuento_dinamico(regla_condicional_lambda, porcentaje=0.10):
    def aplicar(precio):
        if regla_condicional_lambda(precio):
            return round(precio * (1 - porcentaje), 2)
        return precio
    return aplicar


if __name__ == "__main__":
    descuento_mayor_100 = crear_descuento_dinamico(lambda p: p > 100, porcentaje=0.15)
    descuento_par = crear_descuento_dinamico(lambda p: p % 2 == 0, porcentaje=0.05)

    print(descuento_mayor_100(150))
    print(descuento_mayor_100(50))
    print(descuento_par(80))
    print(descuento_par(81))
