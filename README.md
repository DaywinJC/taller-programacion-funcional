# Taller: programación funcional en Python

Veinte ejercicios de closures, lambdas y funciones de orden superior, organizados en cuatro niveles.

## Ejecución

Requiere Python 3.10 o posterior. No necesita paquetes externos.

```console
python ejecutar_todo.py
python verificar.py
python nivel2/09_crear_limitador_avanzado.py
```

`nivel1` a `nivel4` contienen cinco ejercicios cada uno. Cada archivo incluye ejemplos con `print()`. `evidencias/ejecuciones.txt` contiene las salidas reales de la revisión. `verificar.py` comprueba resultados y casos límite mediante aserciones; debe ejecutarse sin la opción `-O`.

## Conceptos y decisiones

Una HOF recibe o devuelve funciones. Un closure conserva variables de su ámbito exterior. Las lambdas permiten inyectar comportamientos. `nonlocal` permite reasignar una variable del ámbito exterior; no es necesario para modificar una lista ya capturada.

1. Formateador: transforma el texto y antepone el prefijo.
2. Operador: la lambda recibe `(valor, factor)`.
3. Descuento: 10 % por defecto; la regla decide si se aplica.
4. Seriales: la lambda recibe nombre y contador. Debe incorporar el contador para lograr unicidad dentro del generador.
5. Divisas: se suma la comisión al importe convertido; representa el total con recargo. Las tasas son ejemplos del ejercicio.
6. Contador: la lambda calcula el nuevo valor a partir del actual, como en los archivos originales.
7. Acumulador: los valores rechazados no alteran el total.
8. Promedio: la lambda devuelve True para conservar un dato; sin datos válidos se devuelve 0 por convención.
9. Limitador: cuenta llamadas desde el último `reset()`; no implementa una ventana de tiempo. La alerta recibe el número de intento rechazado.
10. Conmutador: copia los estados y recorre su orden de forma cíclica; rechaza listas vacías.
11. Colección: filtra antes de transformar con `filter` y `map`.
12. Agrupador: las claves devueltas deben ser hashables.
13. Rastreador: cada llamada al closure ejecuta N veces la tarea y acumula resultados. `.historial()` devuelve una copia superficial sin ejecutar la tarea.
14. Composición: primero g, después f.
15. Auditoría: registra nombre, segundos y resultado de ejecuciones exitosas. Las excepciones de la tarea se propagan.
16. Validador: exige todas las reglas. Sin reglas devuelve True. Incluye el alias con tilde del enunciado.
17. Caché: capacidad positiva y política LRU (menos recientemente usado). Recibe argumentos posicionales hashables; no hay expiración temporal. `.cache_info()` devuelve una copia superficial.
18. Pipeline: aplica funciones de izquierda a derecha; vacío devuelve el dato original.
19. Pub/Sub: devuelve un closure gestor: `bus('suscribirse', evento, callback)` y `bus('emitir', evento, dato)`. Una excepción de un suscriptor se propaga.
20. Consultor: acepta diccionarios y objetos; un campo ausente produce None, que la lambda debe contemplar si corresponde.

## Resultados

Los ejemplos aleatorios usan semilla para que se puedan repetir. La duración de la auditoría cambia entre ejecuciones. Las comprobaciones incluyen aislamiento de estado, reinicio del limitador, reemplazo LRU y entradas inválidas.
