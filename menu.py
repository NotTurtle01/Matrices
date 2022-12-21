#Menu

from modulo.py import *

vacia = matriz([])

d = {}

def guardar(lista):
    print('Quiere guardar la matriz o descartarla?\n')
    print('1: Guardar la matriz')
    print('2: Descartar la matriz')
    opcion = intmayor0('la opción que desea')
    if opcion == 1:
        nombre = str(input('Dime el nombre con el que quieres guardar la matriz: '))
        d[nombre] = matriz(lista)
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
            lista = vacia.crearmatriz(filas,columnas)
            guardar(lista)
         
        elif opcion == 2:
            filas = intmayor0('fila del elemento')
            columnas = intmayor0('columna del elemento')
            elemento = floatlibre('dime el elemento que quieres asignar')
            lista = A.asignar_elemento(filas,columnas,elemento)
            guardar(lista)
        
        elif opcion == 3:
            filas = intmayor0('fila del elemento que quieres mostrar: ')
            columnas = intmayor0('columna del elemento que quieres mostrar: ')
            lista = A.mostrar_objeto(filas,columnas)
            guardar(lista)
        
        elif opcion == 4:
            print(A)

        elif opcion == 5:
            fila = intmayor0('dame la fila: ')
            lista = A.fila(fila)
            print(lista)
        
        elif opcion == 6:
            columna = intmayor0('dame la columna: ')
            lista = A.columna(columna)
            print(lista)
        
        elif opcion == 7:
            diagonal = intmayor0('1) Diagonal principal 2) Diagonal inversa')
            lista = A.diagonal(diagonal)
            print(lista)
    
    return opcion

A = [ [1, 2, 3], [2, 12, 6], [1, 0, -3], [0, -1, 0] ]
