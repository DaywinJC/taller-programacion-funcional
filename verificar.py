"""Comprobaciones reproducibles de los 20 ejercicios y sus casos limite."""
from pathlib import Path
from types import SimpleNamespace
import runpy

ROOT = Path(__file__).resolve().parent
def funcion(numero, nombre):
    archivo = next(ROOT.glob(f'nivel*/{numero:02d}_*.py'))
    return runpy.run_path(str(archivo))[nombre]

def verificar():
    assert funcion(1, 'crear_formateador')('> ', lambda x: x.upper())('hola') == '> HOLA'
    assert funcion(2, 'crear_operador')(3, lambda x, f: x*f)(4) == 12
    d = funcion(3, 'crear_descuento_dinamico')(lambda p: p>100)
    assert (d(100), d(200)) == (100, 180)
    g = funcion(4, 'crear_generador_sufijos')(lambda s, n: f'{s}-{n}')
    assert (g('a'), g('a')) == ('a-1', 'a-2')
    assert funcion(5, 'crear_conversor')(2, lambda x: x*.1)(10) == 22
    c = funcion(6, 'crear_contador_paso')(lambda n: n+3)
    otro = funcion(6, 'crear_contador_paso')(lambda n: n+3)
    assert (c(), c(), otro()) == (3, 6, 3)
    a = funcion(7, 'crear_acumulador_validado')(lambda v: v>0)
    assert (a(-2), a(3), a(4)) == (0, 3, 7)
    p = funcion(8, 'crear_promediador_filtrado')(lambda v: 0<=v<=100)
    assert (p(999), p(20), p(40), p(-10)) == (0, 20, 30, 30)
    alertas=[]
    l = funcion(9, 'crear_limitador_avanzado')(2, alertas.append)
    assert [l(), l(), l()] == [True, True, False] and alertas == [3]
    l.reset()
    assert l() is True
    estados=['a', 'b']
    s = funcion(10, 'crear_conmutador')(estados)
    estados.clear()
    assert [s(), s(), s()] == ['a', 'b', 'a']
    assert funcion(11, 'procesar_coleccion')([1,2,3,4], lambda n:n%2==0, lambda n:n*n) == [4,16]
    assert funcion(12, 'agrupar_por')([{'k':1}, {'k':1}], lambda x:x['k']) == {1:[{'k':1}, {'k':1}]}
    llamadas=[]
    r = funcion(13, 'ejecutar_y_rastrear')(lambda: llamadas.append(1) or len(llamadas), 2)
    assert r() == [1,2] and r() == [1,2,3,4]
    copia=r.historial(); copia.clear()
    assert r.historial() == [1,2,3,4]
    assert funcion(14, 'componer_dos')(lambda n:n*2, lambda n:n+1)(5) == 12
    logs=[]
    auditada=funcion(15, 'auditar_ejecucion')(lambda n:n+1, lambda *informe:logs.append(informe))
    assert auditada(5)==6 and len(logs)==1 and logs[0][1]>=0 and logs[0][2]==6
    v=funcion(16, 'crear_validador_multiple')(lambda n:n>0, lambda n:n%2==0)
    assert v(2) and not v(3)
    llamadas=[]
    m=funcion(17, 'memoizar_avanzado')(lambda n:llamadas.append(n) or n*n, 2)
    assert [m(2), m(3), m(2), m(4)] == [4,9,4,16]
    assert llamadas==[2,3,4] and list(m.cache_info())==[(2,), (4,)]
    m(3); assert llamadas==[2,3,4,3]
    assert funcion(18, 'crear_pipeline')(lambda n:n+2, lambda n:n*3)(4)==18
    assert funcion(18, 'crear_pipeline')()(4)==4
    bus=funcion(19, 'crear_sistema_eventos')(); eventos=[]
    assert callable(bus)
    bus('suscribirse', 'dato', lambda x:eventos.append(x))
    bus('suscribirse', 'dato', lambda x:eventos.append(x*2))
    bus('emitir', 'dato', 3); bus('emitir', 'sin_suscriptores', 1)
    assert eventos==[3,6]
    q=funcion(20, 'crear_consultor')('precio')(lambda p:p is not None and p>10)
    objeto=SimpleNamespace(precio=20)
    assert q([{'precio':5}, {}, objeto])==[objeto]
    for numero, nombre, args in [(9,'crear_limitador_avanzado',(0,print)), (10,'crear_conmutador',([],)), (13,'ejecutar_y_rastrear',(lambda:1,-1)), (17,'memoizar_avanzado',(lambda x:x,0))]:
        try:
            funcion(numero,nombre)(*args)
        except ValueError:
            pass
        else:
            raise AssertionError(f'Falta validar ejercicio {numero}')
    print('CORRECTO: 20 ejercicios verificados; incluye aislamiento, reset, LRU y casos limite.')

if __name__ == '__main__':
    verificar()
