
#Módulo Matrices.

#Definición matrices:



class matriz:
  def __init__(self,lista):
    self.matriz = lista
    self.filas = len(lista)
    self.columnas = len(lista[0])

A = matriz([2,3],[1,2])
