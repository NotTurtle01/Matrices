#Menu

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
        opcion = int(input('Escoge opción: '))
    return opcion



