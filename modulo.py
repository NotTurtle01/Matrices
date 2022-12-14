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
   
  def __str__(self):
    cadena = 'Tu matriz es: {0}\n'.format(self.matriz)
    return cadena

  def __len__(self):
    contador = 0
    for i in self.matriz:
        contador += 1
    return contador

A = matriz([[2,4],[1,2]])
print(A)

