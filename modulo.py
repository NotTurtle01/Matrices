#Módulo Matrices.

#Definición matrices:


class matriz:
  def __init__(self,lista):
    self.matriz = lista
    self.filas = len(lista)
    self.columnas = len(lista[0])
    for fila in lista:
      if len(fila) != len(lista[0]):
        print('Tu lista no es una matriz')
   
  def __str__

A = matriz([2,3],[1,2])
