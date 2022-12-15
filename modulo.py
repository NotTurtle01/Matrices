#Óscar Mirás Sánchez. Joel Rubio González.

#Módulo de Python: class matriz.

class matriz:
    def __init__(self,lista):
        if lista == []:
            self.matriz = lista
        else:
            for fila in lista:
                if len(fila) != len(lista[0]):
                    print('Eso no es una matriz válida')
                    quit()
            self.matriz = lista
            self.filas = len(lista)
            self.columnas = len(lista[0])

    def __str__(self):
        cadena = ''
        for i in range(0,len(self.matriz)):
            if i != (len(self.matriz)-1):
                cadena = cadena + str(self.matriz[i]) + '\n'
            else:
                cadena = cadena + str(self.matriz[i])
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
      lista_diagonal_1 = []
      for i in range(self.columnas):
        lista_diagonal_1.append(self.matriz[i][i])
      return lista_diagonal_1
    if d == 2:
      lista_diagonal_2 = []
      for i in range(self.columnas):
        lista_diagonal_2.append(self.matriz[self.filas -1 - i][i])
      return lista_diagonal_2
    
  def escalar_matriz(self,escalar):
    for fila in range(self.columnas):
      for columna in range(self.filas):
          self.matriz[fila][columna] = escalar * self.matriz[fila][columna]
    return self.matriz

  def opuesta(self):
    return self.escalar_matriz(-1) #Uso recursivo de la función escalar_matriz
  
  def identidad(self,n):
    M = []
    for i in range(n):
      M.append([0] * n )
    for i in range(n):
      M[i][i] = 1
    return M
      
A = matriz([[2,3,4], [1,2,5], [9,2,3]])
print(A.identidad(9))
