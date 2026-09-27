"""
Ejercicio 10: Interruptor Multiple (Maquina de Estados Ligera)
crear_conmutador(lista_estados) alterne ciclicamente entre una lista de
estados internos privados en cada llamada.
"""


def crear_conmutador(lista_estados):
    estados = tuple(lista_estados)
    if not estados:
        raise ValueError("Se requiere al menos un estado")
    indice = -1

    def siguiente_estado():
        nonlocal indice
        indice = (indice + 1) % len(estados)
        return estados[indice]
    return siguiente_estado


if __name__ == "__main__":
    semaforo = crear_conmutador(["rojo", "amarillo", "verde"])

    print(semaforo())
    print(semaforo())
    print(semaforo())
    print(semaforo())  # vuelve a rojo
