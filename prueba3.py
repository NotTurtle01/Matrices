def cargar(archivo):
    archivo = open(archivo, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

print(cargar('matricesprueba.txt'))

def guardar(archivo):
    contenido = 'hola'
    archivo = open(archivo, 'w')
    archivo.write(contenido)
    archivo.close()

print(guardar('nuevo1_texto.txt'))

import six
if six.PY2:
    input("Press the <ENTER> key to continue...")
else:
    input("Press the <ENTER> key to continue...")
