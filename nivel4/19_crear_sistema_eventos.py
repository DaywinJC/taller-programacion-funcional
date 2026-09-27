"""
Ejercicio 19: Sistema Pub/Sub (Event Listener con HOFs y Closures)
Crea crear_sistema_eventos() que devuelva un closure gestor capaz de
registrar suscriptores (lambdas) y emitir eventos notificando a cada
uno.
"""


def crear_sistema_eventos():
    suscriptores = {}

    def suscribirse(evento, fn_callback):
        suscriptores.setdefault(evento, []).append(fn_callback)

    def emitir(evento, *args, **kwargs):
        for callback in tuple(suscriptores.get(evento, [])):
            callback(*args, **kwargs)

    def gestor(accion, evento, *args, **kwargs):
        if accion == "suscribirse":
            return suscribirse(evento, *args, **kwargs)
        if accion == "emitir":
            return emitir(evento, *args, **kwargs)
        raise ValueError("Accion desconocida: " + str(accion))

    return gestor


if __name__ == "__main__":
    bus = crear_sistema_eventos()

    bus("suscribirse", "login", lambda usuario: print(f"Bienvenido, {usuario}"))
    bus("suscribirse", "login", lambda usuario: print(f"[LOG] {usuario} inicio sesion"))
    bus("suscribirse", "logout", lambda usuario: print(f"Hasta luego, {usuario}"))

    bus("emitir", "login", "Ana")
    bus("emitir", "logout", "Ana")
