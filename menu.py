#Menu

from modulo.py import *

vacia = matriz([])

d = {}

def guardar(lista):
    print('\nQuiere guardar la matriz o descartarla?\n')
    print('1: Guardar la matriz')
    print('2: Descartar la matriz')
    opcion = intmayor0('\nLa opción que desea: ')
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
            filas = intmayor0('Número de filas: ')
            columnas = intmayor0('Número de columnas: ')
            lista = vacia.crearmatriz(filas,columnas)
            guardar(lista)
         
        elif opcion == 2:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            filas = intmayor0('Fila del elemento: ')
            columnas = intmayor0('Columna del elemento: ')
            elemento = floatlibre('Elemento que quieres asignar: ') #Se sobreescribirá el elemento a la matrz ya existente.
            d[nombre].asignarelemento(filas,columnas,elemento)
            print(d[nombre]) 

        elif opcion == 3:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            filas = intmayor0('Fila del elemento que quieres mostrar: ')
            columnas = intmayor0('Folumna del elemento que quieres mostrar: ')
            print(d[nombre].mostrarelemento(filas,columnas))
            
        elif opcion == 4:
            print('Estas son las matrices disponibles: ')
            print(d.keys())
            nombre = str(input('Nombre de la matriz que quieres mostrar por pantalla: '))
            print(d[nombre])

        elif opcion == 5:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            fila = intmayor0('Fila: ')
            lista = d[nombre].fila(fila)
            print(lista)
        
        elif opcion == 6:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            columna = intmayor0('Columna: ')
            lista = d[nombre].columna(columna)
            print(lista)
        
        elif opcion == 7:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            diagonal = intmayor0('1) Diagonal principal 2) Diagonal inversa')
            lista = d[nombre].diagonal(diagonal)
            print(lista)
        
        elif opcion == 8:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            dimensiones = d[nombre].dimensiones()
            print('La matriz tiene de dimensiones: ' + str(dimensiones[0]) + ' filas y ' + str(dimensiones[1]) + ' columnas')
            
        elif opcion == 9:
            nombre1 = str(input('Nombre de la primera matriz que quieres utilizar:'))
            nombre2 = str(input('Nombre de la segunda matriz que quieres utilizar:'))
            try:
                lista = d[nombre1] + d[nombre2]
                print(lista)
                guardar(lista)
            except IndexError:
                print('Las matrices no tienen las dimensiones adecuadas para poder sumarse.')
                
        elif opcion == 10:
            nombre1 = str(input('Nombre de la primera matriz que quieres utilizar:'))
            nombre2 = str(input('Nombre de la segunda matriz que quieres utilizar:'))
            try:
                lista = d[nombre1] - d[nombre2]
                print(lista)
                guardar(lista)
            except IndexError:
                print('Las matrices no tienen las dimensiones adecuadas para poder restarse.')
            
        elif opcion == 11:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            lista = d[nombre].opuesta()
            print(lista)
            guardar(lista)
        
        elif opcion == 12:
            nombre1 = str(input('Nombre de la primera matriz que quieres utilizar:'))
            nombre2 = str(input('Nombre de la segunda matriz que quieres utilizar:'))
            try:
                lista = d[nombre1] * d[nombre2]
                print(lista)
                guardar(lista)
            except IndexError:
                print('Las matrices no tienen las dimensiones adecuadas para poder multiplicarse.')
                
        elif opcion == 13:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            num = intlibre('Número por el que quieres multiplicar: ')
            lista = d[nombre].escalar_matriz(num)
            print(lista)
            guardar(lista)
        
        elif opcion == 14:
            filas = intmayor0('Número de filas: ')
            columnas = intmayor0('Número de columnas: ')
            lista = vacia.nula(filas,columnas)
            print(lista)
            guardar(lista)
        
        elif opcion == 15:
            orden = intmayor0('Orden de la matriz identidad: ')
            lista = vacia.identidad(orden)
            print(lista)
            guardar(lista)

        elif opcion == 16:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            lista = d[nombre].transposicion()
            print(lista)
            guardar(lista)
            
        elif opcion == 17:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            if d[nombre].es_magica():
                print('La matriz que ha seleccionado es mágica')
            else:
                print('La matriz que ha seleccionado no es mágica')
                
        elif opcion == 18:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            if d[nombre].is_cuadrada():
                print('La matriz que ha seleccionado es cuadrada')
            else:
                print('La matriz que ha seleccionado no es cuadrada')
        
        elif opcion == 19:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            if d[nombre].is_fila():
                print('La matriz que ha seleccionado es una matriz fila')
            else:
                print('La matriz que ha seleccionado no es una matriz fila')
        
        elif opcion == 20:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            if d[nombre].is_columna():
                print('La matriz que ha seleccionado es una matriz columna')
            else:
                print('La matriz que ha seleccionado no es una matriz columna')
        
        elif opcion == 21:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            if d[nombre].is_simetrica():
                print('La matriz que ha seleccionado es una matriz simétrica')
            else:
                print('La matriz que ha seleccionado no es una matriz simétrica')
        
        elif opcion == 22:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            if d[nombre].is_triangular_superior():
                print('La matriz que ha seleccionado es una matriz triangular superior')
            else:
                print('La matriz que ha seleccionado no es una matriz triangular superior')
                
        elif opcion == 23:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            print('El valor mínimo es: ', d[nombre].minimo())
            
        elif opcion == 24:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            print('El valor máximo es: ', d[nombre].maximo())
            
        elif opcion == 25:
            nombre = str(input('Nombre de la matriz que quieres utilizar: '))
            print('El valor medio es: ', d[nombre].media())
            
    return opcion

A = matriz([ [1, 2, 3], [2, 12, 6], [1, 0, -3], [0, -1, 0] ])
