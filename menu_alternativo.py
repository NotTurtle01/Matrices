
from modulo import *

vacia = matriz([])

d = {}

def guardar(lista):   #Esta función guarda una matriz en el diccionario.
    print('\nQuiere guardar la matriz o descartarla?\n')
    print('1: Guardar la matriz')
    print('2: Descartar la matriz')
    opcion = intmayor0('\nDime la opción que desea: ')
    if opcion == 1:
        nombre = str(input('\nDime el nombre con el que quieres guardar la matriz: '))
        d[nombre] = matriz(lista)
    elif opcion == 2:
        menu()

def mostrardiccionario():  #Función que muestra las entradas del diccionario
    print('\nEstas son las matrices disponibles: ')
    for clave in d.keys():
        print(clave)
        print(d[clave])

def comprobdic():   #Función que comprueba si el diccionario esta vacio.
    if len(d) == 0:
        return 'vacio'
    else:
        return 'no vacio'

def nombrevalido(cadena = 'Dime el nombre de la matriz que quieras utilizar: '):   #Función que comprueba que un nombre esta en el diccionario
    valido = False
    while not valido:
        nombre = str(input(cadena))
        if nombre not in d.keys():
            print('No se ha encontrado esa matriz')
        else:
            valido = True
    return nombre

def espera(): #Función que solicita "input" hasta que el usuario pulsa la tecla <ENTER>
    a = 0
    while a != '':
        a = input('Pulsa <ENTER> para continuar: ')
        
def guardar_archivo(d, archivo):
  contenido = ''
  for i in d.keys():
    contenido += i + "*" + str(d[i].filas) + "*" + str(d[i].columnas) + "*" + str(d[i].resize()) + '\n'

#Como la matriz se imprime con saltos de línea de forma predeterminada, se emplea la función resize()
#con el objetivo de imprimir la matriz en una sola línea. Además, se marcan los espacios entre i (nombre de la matriz)
#el número de filas (d[i].filas), el número de columnas (d[i].columnas) y la matriz a imprimir con el caracter *
#De esta forma se conservarán estos espacios al eliminar el caracter " " posteriormente.

  caracteres = '[]" "'
  resultado = ''.join(x for x in contenido if x not in caracteres) #Sintaxis para eliminar los caracteres '[' ']' y " "
  resultado = resultado.replace("*", " ") 
  #Se lleva a cabo la sustitución de los caracteres * por espacios para construir en resultado la tabla de matrices adecuada.
  archivo = open(archivo, 'w')
  archivo.write(resultado)
  archivo.close()
    
def cargar_archivo(archivo):        #La función guardararchivo guarda las matrices siguiendo un formato: 'nombre' 'filas' 'columnas' 'contenido'. La función de cargar va cogiendo 
    archivo = open(archivo, 'r')    #cada una de estas posiciones y las va utilizando para crear la entrada del diccionario que le corresponde a cada matriz.
    linea = archivo.readline()
    while linea != '':
        lista = linea.split(' ')
        contenido = lista[3].replace(',',' ')
        contenido = contenido.split()
        numeros = []
        for i in range(int(lista[1])):
            fila = []
            for j in range(int(lista[2])):
                fila.append(float(contenido[0]))
                del(contenido[0])
            numeros.append(fila)
        d[lista[0]] = matriz(numeros)
        linea = archivo.readline()
    archivo.close()

def menu():
    print('\n-1: Salir del menu                               11: Obtener la matriz opuesta')
    print('1: Crear una matriz.                             12: Producto de matrices')
    print('2: Asignarle un elemento a una matriz            13: Producto de un escalar por una matriz')
    print('3: Obtener un elemento de una matriz             14: Generar la matriz nula')
    print('4: Imprimir una matriz por pantalla              15: Generar la matriz de identidad')
    print('5: Obtener una fila                              16: Trasponer una matriz')
    print('6: Obtener una columna                           17: Tipo de matriz')
    print('7: Obtener diagonal de una matriz                18: Valor mínimo, máximo y medio de una matriz')
    print('8: Dimensiones de una matriz                     19: Guardar matrices')
    print('9: Sumar dos matrices                            20: Cargar matrices')
    print('10: Restar dos matrices')
    opcion = intlibre('\nDime la opcion que desea: ')
    
    while opcion != -1 and opcion not in range(1,26):
        print('Esa no es una opción válida')
        opcion = intlibre('Dime la opcion que desea:')

    if opcion == 1:  #Esta opción sirve para crear una matriz
        filas = intmayor0('\nDime cuantas filas quieres que tenga la matriz: ')
        columnas = intmayor0('Dime cuantas columnas quieres que tenga la matriz: ')
        print()
        lista = vacia.crearmatriz(filas,columnas)
        print('\nEsta es la matriz resultante: ')
        print(lista)
        espera()
        guardar(lista)
        menu()

    elif opcion == 2:  #Esta opción le asigna un elemento a una matriz
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opcion\n')
            time.sleep(2)
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            fila = intmayor0('\nDime la fila del elemento: ')
            while fila > d[nombre].dimensiones()[0]:
                print('No existe esa fila')
                fila = intmayor0('\nDime la fila del elemento: ')
            columna = intmayor0('\nDime la columna del elemento: ')
            while columna > d[nombre].dimensiones()[1]:
                print('No existe esa columna')
                columna = intmayor0('\nDime la columna del elemento: ')
            elemento = floatlibre('\nDime el elemento que quieres asignar: ')
            d[nombre].asignarelemento(fila,columna,elemento)
            print('\nEsta es la matriz resultante: ')
            print(d[nombre])
            espera()
        menu()

    elif opcion == 3:    #Esta opción muestra un elemento de una matriz
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opcion\n')
            espera()
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            fila = intmayor0('\nDime la fila del elemento que quieres mostrar: ')
            while fila > d[nombre].dimensiones()[0]:
                print('No existe esa fila')
                fila = intmayor0('\nDime la fila del elemento: ')
            columna = intmayor0('\nDime la columna del elemento que quieres mostrar: ')
            while columna > d[nombre].dimensiones()[1]:
                print('No existe esa columna')
                columna = intmayor0('\nDime la columna del elemento: ')
            print('El elemento de esa fila y esa columna es: ',d[nombre].mostrarelemento(fila,columna))
            espera()
        menu()

    elif opcion == 4:    #Esta opción imprime una matriz por pantalla.
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opcion\n')
            espera()
        else:
            print('\nEstas son las matrices disponibles para imprimir: ')
            for clave in d.keys():
                print(clave)
            nombre = nombrevalido()
            print('\nEsta es la matriz', nombre, ': ')
            print(d[nombre])
            espera()
        menu()
    
    elif opcion == 5:   #Esta opción obtiene una fila de una matriz
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opcion\n')
            espera()
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            fila = intmayor0('\nDime la fila que quieras obtener: ')
            lista = d[nombre].fila(fila)
            print('\nEsta es la fila seleccionada: ', lista)
            espera()
        menu()

    elif opcion == 6:    #Esta opción obtiene una columna de una matriz
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opcion\n')
            espera()
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            columna = intmayor0('\nDime la columna que quieras obtener: ')
            lista = d[nombre].columna(columna)
            print('\nEsta es la columna seleccionada: ', lista)
            espera()
        menu()

    elif opcion == 7:   #Esta opción obtiene una diagonal de una matriz
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opcion\n')
            espera()
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
            espera()
        menu()

    elif opcion == 8:   #Esta opción devuelve las dimensiones
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            espera()
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            dimensiones = d[nombre].dimensiones()
            print('\nLa matriz tiene de dimensiones: ' + str(dimensiones[0]) + ' filas y ' + str(dimensiones[1]) + ' columnas\n')
            espera()
        menu()

    elif opcion == 9:   #Esta opción suma matrices
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            espera()
        else:
            mostrardiccionario()
            nombre1 = nombrevalido('Dime el nombre de la primera matriz que quieras sumar: ')
            nombre2 = nombrevalido('Dime el nombre de la segunda matriz que quieras sumar: ')
            lista = d[nombre1] + d[nombre2]
            if lista != None:
                print('\nEsta es la matriz suma: ', lista)
                espera()
                guardar(lista)
            else:
                espera()
        menu()

    elif opcion == 10:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            espera()
        else:
            mostrardiccionario()
            nombre1 = nombrevalido('Dime el nombre de la primera matriz que quieras utilizar: ')
            nombre2 = nombrevalido('Dime el nombre de la segunda matriz que quieras restar: ')
            lista = d[nombre1] - d[nombre2]
            if lista != None:
                print('\nEsta es la matriz resta: ', lista)
                espera()
                guardar(lista)
            else:
                espera()
        menu()

    elif opcion == 11:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            espera()
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            lista = d[nombre].opuesta()
            print('\nEsta es la matriz opuesta: ', lista)
            espera()
            guardar(lista)
        menu()

    elif opcion == 12:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            espera()
        else:
            mostrardiccionario()
            nombre1 = nombrevalido('Dime el nombre de la primera matriz que quieras utilizar: ')
            nombre2 = nombrevalido('Dime el nombre de la segunda matriz que quieres multiplicar: ')
            lista = d[nombre1] * d[nombre2]
            if lista != None:
                print('\nEsta es la matriz multiplicación: ', lista)
                espera()
                guardar(lista)
            else:
                espera()
        menu()

    elif opcion == 13:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            espera()
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            num = intlibre('Dime el escalar por el que quieres multiplicar: ')
            lista = d[nombre].escalar_matriz(num)
            print('\nLa matriz resultante es: ', lista)
            espera()
            guardar(lista)
        menu()
    
    elif opcion == 14:
        filas = intmayor0('\nDime el número de filas: ')
        columnas = intmayor0('Dime el número de columnas: ')
        lista = vacia.nula(filas,columnas)
        print('\nEsta es la matriz nula: ', lista)
        espera()
        guardar(lista)
        menu()

    elif opcion == 15:
        orden = intmayor0('\nDime el orden de la matriz de identidad: ')
        lista = vacia.identidad(orden)
        print('Esta es la matriz de identidad: ', lista)
        espera()
        guardar(lista)
        menu()

    elif opcion == 16:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            espera()
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            lista = d[nombre].transposicion()
            print('\nLa matriz traspuesta es: ', lista)
            espera()
            guardar(lista)
        menu()

    elif opcion == 17:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            espera()
        else:
            print('\n1) Mágica')
            print('2) Cuadrada')
            print('3) Fila')
            print('4) Columna')
            print('5) Simétrica')
            print('6) Triangular superior')
            print('7) Triangular inferior')
            nueva_opcion = int(input('\nOpción: '))

            while nueva_opcion not in range (1,8):
                print('Esa no es una opción válida')
                nueva_opcion = intlibre('Opción: ')
            
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

            espera()
            menu()

    elif opcion == 18:
        if comprobdic() == 'vacio':
            print('\nNo hay ninguna matriz guardada sobre la que aplicar esta opción\n')
            espera()
        else:
            mostrardiccionario()
            nombre = nombrevalido()
            print('El valor mínimo es: ', d[nombre].minimo())
            print('El valor máximo es: ', d[nombre].maximo())
            print('El valor medio es: ', d[nombre].media())
            espera()
        menu()
    
    elif opcion == 19:
        archivo = str(input('\nDime el nombre del archivo en el que quieres guardar las matrices: '))
        guardar_archivo(d, archivo)
        print('\nLas matrices han sido guardadas en', archivo)
        espera()
        menu()
    
    elif opcion == 20:
        archivo = str(input('\nDime el nombre del archivo del que quieres cargar las matrices: '))
        cargar_archivo(archivo)
        print('\nLas matrices han sido cargadas\n')
        espera()
        menu()

menu()
