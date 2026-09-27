"""
Ejercicio 5: Conversor de Divisas con Margen
crear_conversor(tasa, margen_lambda) retorna una funcion para convertir
montos calculando dinamicamente la comision adicional.
"""


def crear_conversor(tasa, margen_lambda):
    def convertir(monto):
        convertido = monto * tasa
        comision = margen_lambda(convertido)
        return round(convertido + comision, 2)
    return convertir


if __name__ == "__main__":
    usd_a_eur = crear_conversor(0.92, lambda m: m * 0.02)
    usd_a_pen = crear_conversor(3.75, lambda m: 5 if m > 200 else 1.5)

    print(usd_a_eur(100))
    print(usd_a_pen(50))
    print(usd_a_pen(300))
