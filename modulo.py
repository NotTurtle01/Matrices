#Óscar Mirás Sánchez. Joel Rubio González.

#Módulo de Python: class matriz.

class matriz:
  def __init__(self,lista):
    self.matriz = lista
    self.filas = len(lista)
    self.columnas = len(lista[0])
    for fila in lista:
      if len(fila) != len(lista[0]):
        print('Tu lista no es una matriz válida')
        quit()
   
  def __str__(self):
    cadena = 'Tu matriz es: {0}\n'.format(self.matriz)
    return cadena
  
  def mostrar_objeto(self,n,m):
    return self.matriz[n-1][m-1]
  
  def asignar_elemento(self,n,m,elemento):
    self.matriz[n-1][m-1] = elemento
    return self.matriz

A = matriz([[2,3], [1,2], [1,5]])
print(A)
print(A.mostrar_objeto(2, 1))
print(A.asignar_elemento(2, 1, 89))
