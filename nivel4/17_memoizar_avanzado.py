"""
Ejercicio 17: Cache con Expiracion o Tamano Maximo (Memoizacion
Profesional)
Crea la HOF memoizar_avanzado(fn_costosa, max_items) que retorne un
closure controlando el estado privado de una memoria cache con limite
de capacidad (politica LRU simple).
"""

from collections import OrderedDict


def memoizar_avanzado(fn_costosa, max_items):
    if not isinstance(max_items, int) or isinstance(max_items, bool) or max_items < 1:
        raise ValueError("max_items debe ser un entero positivo")
    cache = OrderedDict()

    def envoltura(*args):
        if args in cache:
            cache.move_to_end(args)
            return cache[args]
        resultado = fn_costosa(*args)
        cache[args] = resultado
        if len(cache) > max_items:
            cache.popitem(last=False)
        return resultado

    envoltura.cache_info = lambda: dict(cache)
    return envoltura


if __name__ == "__main__":
    def cuadrado_costoso(n):
        print(f"  (calculando cuadrado de {n})")
        return n * n

    cuadrado_cacheado = memoizar_avanzado(cuadrado_costoso, max_items=2)

    print(cuadrado_cacheado(2))
    print(cuadrado_cacheado(3))
    print(cuadrado_cacheado(2))  # desde cache
    print(cuadrado_cacheado(4))  # descarta el 3 (LRU)
    print(cuadrado_cacheado.cache_info())
