#Menu

from modulo.py import *

vacia = matriz([])

d = {}

def guardar(matriz):
    print('Quiere guardar la matriz o descartarla?\n')
    print('1: Guardar la matriz')
    print('2: Descartar la matriz')
    opcion = intmayor0('la opción que desea')
    if opcion == 1:
        nombre = str(input('Dime el nombre con el que quieres guardar la matriz: '))
        d[nombre] = matriz
        print(d)
    elif opcion == 2:
        quit()

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
        
        if opcion == 1:
            filas = intmayor0('cuantas filas quieres que tenga la matriz')
            columnas = intmayor0('cuantas columnas quieres que tenga la matriz')
            matriz = vacia.crearmatriz(filas,columnas)
            guardar(matriz)
         
        elif opcion == 2:
            
    
    return opcion




