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
    cadena = ''
    for i in self.matriz:
      if i != self.matriz[-1]:
        cadena = cadena + str(i) + '\n'
      else:
        cadena = cadena + str(i)
    return cadena
  
  def mostrar_objeto(self,n,m):
    return self.matriz[n-1][m-1]
  
  def asignar_elemento(self,n,m,elemento):
    self.matriz[n-1][m-1] = elemento
    return self.matriz

  def fila(self,n):
    return self.matriz[n-1]
  
  def columna(self,m):
    lista_columna = []
    for i in self.matriz:
      lista_columna.append(i[m-1])
    return lista_columna

  def diagonal(self,d):
    if d == 1:
      


A = matriz([[2,3], [1,2], [1,5]])
print(A.columna(1))
