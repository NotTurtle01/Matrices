#Menu

from modulo.py import *

def menu():
    opcion = 0
    while opcion == 0:
        print('1) Definición de una matriz de unas dimensiones dadas')
        print('2) Asignación de un elemento específico de una matriz')
        print('3) Obtención de un elemento específico de una matriz')
        print('4) Presentación de una matriz por pantalla')
        print('5) Obtención de una fila')
        print('6) Obtención de una columna')
        print('7) Obtención de una diagonal')
        print('8) Devolución de dimensiones')
        print('9) Sumar matrices')
        print('10) Restar matrices')
        print('11) Obtener la matriz opuesta')
        print('12) Multiplicar matrices')
        print('13) Producto de escalar por matriz')
        print('14) Generar matriz nula')
        print('15) Generar matriz identidad')
        print('16) Trasponer una matriz')
        print('17) Tipo de matriz')
        print('18) Obtención valor máximo')
        print('19) Obtención valor mínimo')
        print('20) Obtención valor medio')
        opcion = int(input('Escoge opción: '))
    return opcion




