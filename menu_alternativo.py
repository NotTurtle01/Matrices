
from matrices import *
import time

vacia = matriz([])

d = {}

def guardar(lista):
    print('\nQuiere guardar la matriz o descartarla?\n')
    print('1: Guardar la matriz')
    print('2: Descartar la matriz')
    opcion = intmayor0('\nDime la opción que desea: ')
    if opcion == 1:
        nombre = str(input('\nDime el nombre con el que quieres guardar la matriz: '))
        d[nombre] = matriz(lista)
    elif opcion == 2:
        menu()

def mostrardiccionario():
    print('\nEstas son las matrices disponibles: ')
    for clave in d.keys():
        print(clave)
        print(d[clave])

def comprobdic():
    if len(d) == 0:
        return 'vacio'
    else:
        return 'no vacio'

def nombrevalido(cadena = 'Dime el nombre de la matriz que quieras utilizar: '):
    valido = False
    while not valido:
        nombre = str(input(cadena))
        if nombre not in d.keys():
            print('No se ha encontrado esa matriz')
        else:
            valido = True
    return nombre


def menu():
    print('-1: Salir del menu')
    print('1: Crear una matriz.')
    print('2: Asignarle un elemento a una matriz')
    print('3: Obtener un elemento de una matriz')
    print('4: Imprimir una matriz por pantalla')
    print('5: Obtener una fila')
    print('6: Obtener una columna')
    print('7: Obtener diagonal de una matriz')
    print('8: Dimensiones de una matriz')
    print('9: Sumar dos matrices')
    print('10: Restar dos matrices')
    print('11: Obtener la matriz opuesta')
    print('12: Producto de matrices')
    print('13: Producto de un escalar por una matriz')
    print('14: Generar la matriz nula')
    print('15: Generar la matriz de identidad')
    print('16: Trasponer una matriz')
    print('17: Comprobar si una matriz es de un tipo')
    print('18: Valor mínimo, máximo y medio de una matriz')
    opcion = intlibre('Dime la opcion que desea: ')
    while opcion != -1 and opcion not in range(1,26):
        print('Esa no es una opción válida')
        opcion = intlibre('Dime la opcion que desea:')


    if opcion == 1:
        filas = intmayor0('\nDime cuantas filas quieres que tenga la matriz: ')
        columnas = intmayor0('\nDime cuantas columnas quieres que tenga la matriz: ')
        print()
        lista = vacia.crearmatriz(filas,columnas)
        print('\nEsta es la matriz resultante: ')
        print(lista)
        time.sleep(2)
        guardar(lista)
        menu()

    elif opcion == 2:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opcion\n')
            time.sleep(2)
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            filas = intmayor0('\nDime la fila del elemento: ')
            columnas = intmayor0('\nDime la columna del elemento: ')
            elemento = floatlibre('\nDime el elemento que quieres asignar: ')
            d[nombre].asignarelemento(filas,columnas,elemento)
            print('\nEsta es la matriz resultante: ')
            print(d[nombre])
            time.sleep(2)
        menu()

    elif opcion == 3:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opcion\n')
            time.sleep(2)
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            filas = intmayor0('\nDime la fila del elemento que quieres mostrar: ')
            columnas = intmayor0('\nDime la columna del elemento que quieres mostrar: ')
            print('El elemento de esa fila y esa columna es: ',d[nombre].mostrarelemento(filas,columnas))
            time.sleep(2)
        menu()

    elif opcion == 4:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opcion\n')
            time.sleep(2)
        else:
            print('\nEstas son las matrices disponibles para imprimir: ')
            for clave in d.keys():
                print(clave)
            nombre = nombrevalido()
            print('\nEsta es la matriz ', nombre, ': ')
            print(d[nombre])
            time.sleep(4)
        menu()
    
    elif opcion == 5:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opcion\n')
            time.sleep(2)
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            fila = intmayor0('\nDime la fila que quieras obtener: ')
            lista = d[nombre].fila(fila)
            print('\nEsta es la fila seleccionada: ', lista)
            time.sleep(4)
        menu()

    elif opcion == 6:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opcion\n')
            time.sleep(2)
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            columna = intmayor0('\nDime la columna que quieras obtener: ')
            lista = d[nombre].columna(columna)
            print('\nEsta es la columna seleccionada: ', lista)
            time.sleep(4)
        menu()

    elif opcion == 7:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opcion\n')
            time.sleep(2)
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            print('\nQue diagonal quieres obtener?\n1: Diagonal principal\n2: Diagonal inversa')
            diagonal = intlibre('Dime la opción que deseas: ')
            while diagonal not in range(1,3):
                print('Esa no es una opción valida, intentelo de nuevo.')
                diagonal = intlibre('Dime la opción que deseas: ')
            lista = d[nombre].diagonal(diagonal)
            print('\nEsta es la diagonal seleccionada: ', lista)
            time.sleep(4)
        menu()

    elif opcion == 8:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            time.sleep(2)
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            dimensiones = d[nombre].dimensiones()
            print('\nLa matriz tiene de dimensiones: ' + str(dimensiones[0]) + ' filas y ' + str(dimensiones[1]) + ' columnas\n')
            time.sleep(4)
        menu()

    elif opcion == 9:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            time.sleep(2)
        else:
            mostrardiccionario()
            nombre1 = nombrevalido('Dime el nombre de la primera matriz que quieras utilizar: ')
            nombre2 = nombrevalido('Dime el nombre de la segunda matriz que quieras utilizar: ')
            lista = d[nombre1] + d[nombre2]
            print('\nEsta es la matriz suma: ', lista)
            time.sleep(2)
            guardar(lista)
        menu()

    elif opcion == 10:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            time.sleep(2)
        else:
            mostrardiccionario()
            nombre1 = nombrevalido('Dime el nombre de la primera matriz que quieras utilizar: ')
            nombre2 = nombrevalido('Dime el nombre de la segunda matriz que quieras utilizar: ')
            lista = d[nombre1] - d[nombre2]
            print('\nEsta es la matriz resta: ', lista)
            time.sleep(2)
            guardar(lista)
        menu()

    elif opcion == 11:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            time.sleep(2)
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            lista = d[nombre].opuesta()
            print('\nEsta es la matriz opuesta: ', lista)
            time.sleep(2)
            guardar(lista)
        menu()

    elif opcion == 12:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            time.sleep(2)
        else:
            mostrardiccionario()
            nombre1 = nombrevalido('Dime el nombre de la primera matriz que quieras utilizar: ')
            nombre2 = nombrevalido('Dime el nombre de la segunda matriz que quieras utilizar: ')
            try:
                lista = d[nombre1] * d[nombre2]
                print('\nEsta es la matriz multiplicación: ', lista)
                time.sleep(2)
                guardar(lista)
                menu()
            except IndexError:
                print('Las matrices no tienen las dimensiones adecuadas para poder multiplicarse.')
        menu()

    elif opcion == 13:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            time.sleep(2)
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            num = intlibre('Dime el número por el que quieres multiplicar: ')
            lista = d[nombre].escalar_matriz(num)
            print('\nLa matriz resultante es: ', lista)
            time.sleep(2)
            guardar(lista)
        menu()
    
    elif opcion == 14:
        filas = intmayor0('\nDime el número de filas: ')
        columnas = intmayor0('\nDime el número de columnas: ')
        lista = vacia.nula(filas,columnas)
        print('\nEsta es la matriz nula: ', lista)
        time.sleep(2)
        guardar(lista)
        menu()

    elif opcion == 15:
        orden = intmayor0('\nDime el orden de la matriz de identidad: ')
        lista = vacia.identidad(orden)
        print('Esta es la matriz de identidad: ', lista)
        time.sleep(2)
        guardar(lista)
        menu()

    elif opcion == 16:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            time.sleep(2)
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            lista = d[nombre].transposicion()
            print('\nLa matriz traspuesta es: ', lista)
            time.sleep(2)
            guardar(lista)
        menu()

    elif opcion == 17:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            time.sleep(2)
        else:
            print('\n1) Mágica')
            print('2) Cuadrada')
            print('3) Fila')
            print('4) Columna')
            print('5) Simétrica')
            print('6) Triangular superior')
            print('7) Triangular inferior')
            nueva_opcion = int(input('\nDime la opción que deseas'))

            while nueva_opcion not in range (1,8):
                print('Esa no es una opción válida')
                nueva_opcion = intlibre('Dime la opción que deseas')
            
            mostrardiccionario()
            nombre = nombrevalido()

            if nueva_opcion == 1:
                if d[nombre].es_magica():
                    print('\nLa matriz que ha seleccionado es mágica')
                else:
                    print('\nLa matriz que ha seleccionado no es mágica')
                
            elif nueva_opcion == 2:
                if d[nombre].is_cuadrada():
                    print('\nLa matriz que ha seleccionado es cuadrada')
                else:
                    print('\nLa matriz que ha seleccionado no es cuadrada')
                
            elif nueva_opcion == 3:
                if d[nombre].is_fila():
                    print('\nLa matriz que ha seleccionado es una matriz fila')
                else:
                    print('\nLa matriz que ha seleccionado no es una matriz fila')
            
            elif nueva_opcion == 4:
                if d[nombre].is_columna():
                    print('\nLa matriz que ha seleccionado es una matriz columna')
                else:
                    print('\nLa matriz que ha seleccionado no es una matriz columna')
                
            elif nueva_opcion == 5:
                if d[nombre].is_simetrica():
                    print('\nLa matriz que ha seleccionado es una matriz simétrica')
                else:
                    print('\nLa matriz que ha seleccionado no es una matriz simétrica')

            elif nueva_opcion == 6:
                if d[nombre].is_triangular_superior():
                    print('\nLa matriz que ha seleccionado es una matriz triangular superior')
                else:
                    print('\nLa matriz que ha seleccionado no es una matriz triangular superior')

            elif nueva_opcion == 7:
                if d[nombre].is_triangular_inferior():
                    print('\nLa matriz que ha seleccionado es una matriz triangular inferior')
                else:
                    print('\nLa matriz que ha seleccionado no es una matriz triangular inferior')

            time.sleep(2)
            menu()

    elif opcion == 18:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            time.sleep(2)
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            print('El valor mínimo es: ', d[nombre].minimo())
            time.sleep(1)
            print('El valor máximo es: ', d[nombre].maximo())
            time.sleep(1)
            print('El valor medio es: ', d[nombre].media())
            time.sleep(4)
        menu()

menu()
