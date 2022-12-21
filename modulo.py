'''
Autores:

Óscar Mirás Sánchez. 
Joel Rubio González.

'''

#Módulo "ClassMatrix" 

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
      
    def crearmatriz(self,n,m):
      defecto = [[0]]
      for i in range(n-1):
          defecto.append([0])
      for i in range(n):
          for j in range(m-1):
              defecto[i].append(0)
      for i in range(n):
          for j in range(m):
              valido = False
              while not valido:
                  try:          
                      defecto[i][j] = float(input('Dime el elemento de la fila ' + str(i+1) + ' ,columna ' + str(j+1) + ': '))
                      valido = True
                  except ValueError:
                      print('Eso no es un número válido, intentelo de nuevo')
      return defecto
      
    def mostrar_elemento(self,n,m):
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
      if not self.is_cuadrada():
        print('La matriz no es cuadrada')
        return False
      else:
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
      
    def nula(self,n,m):
      lista_nula = [[0]]
      for i in range(n-1):
          lista_nula.append([0])
      for i in range(n):
          for j in range(m-1):
              lista_nula[i].append(0)
      return lista_nula

    def __add__(self,otro):
        if otro.filas != self.filas:
            print('Como las matrices no tienen las mismas dimensiones no se pueden sumar')
        elif otro.columnas != self.columnas:
            print('Como las matrices no tienen las mismas dimensiones no se pueden sumar')
        else:
            suma = []
            for i in range(self.filas):
                fila = []
                for j in range(self.columnas):
                    fila.append(self.matriz[i][j] + otro.matriz[i][j])
                suma.append(fila)
        return suma

    def __sub__(self,otro):
        if otro.filas != self.filas:
            print('Como las matrices no tienen las mismas dimensiones no se pueden restar')
        elif otro.columnas != self.columnas:
            print('Como las matrices no tienen las mismas dimensiones no se pueden restar')
        else:
            resta = []
            for i in range(self.filas):
                fila = []
                for j in range(self.columnas):
                    fila.append(self.matriz[i][j] - otro.matriz[i][j])
                resta.append(fila)
        return resta
    
    def transposicion(self):
      lista_nula = [[0]]
      for i in range(self.columnas -1):
          lista_nula.append([0])
      for i in range(self.columnas):
          for j in range(self.filas -1):
              lista_nula[i].append(0)
      for i in range (self.filas):
        for j in range (self.columnas):
          lista_nula[i][j] = self.matriz[j][i]
      return lista_nula
    
    def is_cuadrada(self):
      if self.filas == self.columnas:
        return True
      else:
        return False
    
    def is_fila(self):
      if self.filas == 1:
        return True
      else:
        return False
    
    def is_columna(self):
      if self.columnas == 1:
        return True
      else: 
        return False
    
    def is_simetrica(self):
      if self.transposicion() == self.matriz:
        return True
      else:
        return False
    
    def is_triangular_superior(self):
      flag = True
      for i in range(1, self.filas):
        for j in range(0, i):
          if self.matriz[i][j] != 0:
                flag = False
      return flag

    def is_triangular_inferior(self):
        self.matriz = self.transposicion() #Uso recursivo de las funciones transposicion() e is_triangular_superior()
        return self.is_triangular_superior()

    def __mul__(self,otro):
        if self.columnas != otro.filas:
            print('Esas matrices no tienen dimensiones validas para multiplicar')
            quit()
        else:
            mul = []
            for i in range(self.filas):
                fila = []
                for j in range(otro.columnas):
                    suma = 0
                    for t in range(otro.columnas):
                        suma += self.matriz[i][t] * otro.matriz[t][j]
                        fila.append(suma)
                mul.append(fila)
            return mul
    
    def es_magica(self):
      if not self.is_cuadrada():
        return False
      else:
        for i in range(1,(self.filas*self.filas)+1):
            presente = False
            for j in range(self.filas):
                for t in range(self.columnas):
                    if self.matriz[j][t] == i:
                        presente = True
            if not presente:
                return False
        sumas = []
        for i in range(self.filas):
            suma = 0
            for j in range(self.columnas):
                suma += self.matriz[i][j]
            sumas.append(suma)
        for i in range(self.columnas):
            suma = 0
            for j in range(self.filas):
                suma += self.matriz[j][i]
            sumas.append(suma)
        suma = 0
        for i in range(self.filas):
            suma += self.matriz[i][i]
        sumas.append(suma)
        suma = 0
        for i in range(self.filas):
            suma += self.matriz[i][-(i+1)]
        sumas.append(suma)
        for i in range(len(sumas)):
            if sumas[0] != sumas[i]:
                return False
        return True

    def minimo(self):
        minimo = self.matriz[0][0]
        for i in range(self.filas):
            for j in range(self.columnas):
                if minimo > self.matriz[i][j]:
                    minimo = self.matriz[i][j]
        return minimo

    
    def maximo(self):
        maximo = self.matriz[0][0]
        for i in range(self.filas):
            for j in range(self.columnas):
                if maximo < self.matriz[i][j]:
                    maximo = self.matriz[i][j]
        return maximo

    def media(self):
        suma = 0
        for i in range(self.filas):
            for j in range(self.columnas):
                suma += self.matriz[i][j]
        media = suma/(self.filas*self.columnas)
        return media

def intmayor0(cadena):
    flag = False
    while flag == False:
        try:
            a = int(input(cadena))
            if a > 0:
                flag = True
            else:
                print('No has introducido un entero positivo. Vuelve a adjuntar el número.')
        except ValueError:
            print('No has introducido un número entero. Inténtalo de nuevo.')
    return a

def floatlibre(a):
    flag = False
    while flag == False:
        try:
            float(a)
            flag = True
        except ValueError:
            print('No has introducido un número flotante. Inténtalo de nuevo.')
            a = input('Dame un flotante: ')
    return float(a)

def intlibre(a):
    flag = False
    while flag == False:
        try:
            int(a)
            flag = True
        except ValueError:
            print('No has introducido un número entero. Inténtalo de nuevo.')
            a = input('Dame un entero: ')
    return int(a)
