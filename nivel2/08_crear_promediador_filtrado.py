"""
Ejercicio 8: Promediador con Eliminacion de Valores Extremos
crear_promediador_filtrado(filtro_ruido_lambda) acumula datos
privadamente pero aplica la lambda para descartar valores atipicos
antes de recalcular el promedio.
"""


def crear_promediador_filtrado(filtro_ruido_lambda):
    datos = []

    def agregar(valor):
        datos.append(valor)
        limpios = [d for d in datos if filtro_ruido_lambda(d)]
        if not limpios:
            return 0
        return round(sum(limpios) / len(limpios), 2)
    return agregar


if __name__ == "__main__":
    # descarta valores fuera del rango 0-100
    promedio_sensor = crear_promediador_filtrado(lambda v: 0 <= v <= 100)

    print(promedio_sensor(20))
    print(promedio_sensor(30))
    print(promedio_sensor(999))  # ruido, se descarta
    print(promedio_sensor(40))
