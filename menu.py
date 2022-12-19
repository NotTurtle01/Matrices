#Menu

def menu():
    opcion = 0
    while opcion != 1 and opcion != 2:
        print('1) Definición de una matriz de unas dimensiones dadas')
        print('2) Asignación de un elemento específico de una matriz')
        print('3) Obtención de un elemento específico de una matriz')
        print('4) Presentación de una matriz por pantalla')
        opcion = int(input('Escoge opción: '))
    return opcion



