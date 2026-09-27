"""
Ejercicio 4: Generador de Seriales / Nombres Unicos
crear_generador_sufijos(patron_lambda) devuelve un closure para
transformar nombres de archivos basandose en una lambda de formato.
Mantiene un contador interno; el patron debe incluirlo para producir nombres unicos.
"""


def crear_generador_sufijos(patron_lambda):
    contador = {"n": 0}

    def generar(nombre_base):
        contador["n"] += 1
        return patron_lambda(nombre_base, contador["n"])
    return generar


if __name__ == "__main__":
    serial_guion = crear_generador_sufijos(lambda nombre, n: f"{nombre}-{n:03d}")
    serial_parentesis = crear_generador_sufijos(lambda nombre, n: f"{nombre}({n})")

    print(serial_guion("reporte"))
    print(serial_guion("reporte"))
    print(serial_guion("reporte"))
    print(serial_parentesis("foto"))
    print(serial_parentesis("foto"))
