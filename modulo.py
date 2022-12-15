#Óscar Mirás Sánchez. Joel Rubio González.

#Módulo de Python: class matriz.

class matriz:
  def __init__(self,lista):
    self.matriz = lista
    self.filas = len(lista)
    self.columnas = len(lista[0])
    for fila in lista:
      if len(fila) != len(lista[0]):
        print('Tu lista no es una matriz')
        quit()
   
  def __str__(self):
    cadena = 'Tu matriz es: {0}\n'.format(self.matriz)
    return cadena

A = matriz([[2,3], [1,2], [1,5,6]])
print(A)


