"""
Ejercicio 20: Mini-Query Engine sobre Listas de Objetos
crear_consultor(campo) devuelve una HOF para generar filtros dinamicos
sobre listas de diccionarios/objetos mediante expresiones lambda
complejas.
"""


def crear_consultor(campo):
    def generar_filtro(fn_condicion_lambda):
        def filtrar(lista_objetos):
            return [obj for obj in lista_objetos if fn_condicion_lambda((obj.get(campo) if isinstance(obj, dict) else getattr(obj, campo, None)))]
        return filtrar
    return generar_filtro


if __name__ == "__main__":
    productos = [
        {"nombre": "Laptop", "precio": 900},
        {"nombre": "Mouse", "precio": 15},
        {"nombre": "Monitor", "precio": 250},
        {"nombre": "Teclado", "precio": 40},
    ]

    consultar_por_precio = crear_consultor("precio")
    caros = consultar_por_precio(lambda p: p > 100)
    baratos = consultar_por_precio(lambda p: p <= 40)

    print(caros(productos))
    print(baratos(productos))
