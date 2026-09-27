"""
Ejercicio 16: Validador Compuesto de Reglas de Negocio
Crea crear_validador_multiple(*lambdas_criterios) que retorne un
closure que evalue si un objeto cumple todas las reglas pasadas como
argumento.
"""


def crear_validador_multiple(*lambdas_criterios):
    def validar(objeto):
        return all(criterio(objeto) for criterio in lambdas_criterios)
    return validar


# Alias que conserva exactamente el nombre del enunciado.
crear_validador_múltiple = crear_validador_multiple


if __name__ == "__main__":
    es_valido_usuario = crear_validador_multiple(
        lambda u: len(u.get("nombre", "")) > 0,
        lambda u: u.get("edad", 0) >= 18,
        lambda u: "@" in u.get("email", ""),
    )

    usuario_ok = {"nombre": "Ana", "edad": 25, "email": "ana@mail.com"}
    usuario_menor = {"nombre": "Luis", "edad": 15, "email": "luis@mail.com"}

    print(es_valido_usuario(usuario_ok))
    print(es_valido_usuario(usuario_menor))
