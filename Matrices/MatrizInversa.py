import numpy as np

def minor(A,i,j): #Calculo del determinante del menor
    m=[]
    rows=len(A)
    cols=rows
    
    for r in range(rows):
      l=[]
      for c in range(cols):
         if c != j:
            l.append(A[r][c])
      if r !=i:
        m.append(l)
    return np.linalg.det(m) #El menor de un elemento aij se denota Mij es el determinante de la matriz resultante al borrar el renglon i y la columna j de  A
  
def comatrix(A):  #Calculo de matriz de cofactores de A
    rows=len(A)
    cols=rows
    c=[]
    for i in range(rows):
        l=[]
        for j in range(cols):
          l.append((-1)**(i+j)*minor(A,i,j)) #Para calcular los cofactres de una matriz se necesita la menor de la cada elemento de la matriz A
                                             #la Formula es Aij = (-1)^(i+j)|Mij|
        c.append(l)    
    return (c)
  
def adjunct(A): #Calculo de matriz adjunta, adjA= transpuesta de matriz de cofactores de A
    return np.transpose(comatrix(A)) 
    
def inverse(A): # Calculo de la Matriz inversa mediante la adjunta. A^-1 = [(A*)^T] / |A|
    '''
    Se pide que el usuario introduzca una matriz de nxn 
	ya que para calacular la inversa esta debe ser una matriz cuadrada

	Consta de una serie de funciones para implementar la formula de la matrizinversa
	
			A^-1 = [(A*)^T] / |A|
			
		La matriz adjunta [(A*)^T] => tambien se conoce como la transpuesta de la matriz de cofactores
		Determinamte de A =>|A| 

	Cada funcion se encarga de genrar una partep para la ecucion.
	Se calcula inicialmente la determinante de la matriz menor de A.
	Posteriormente se calcula la matriz de cofactores usando la siguiente fórmula
	
			Aij = (-1)^(i+j)|Mij|

	Una vez calculada la matríz de cofactores generamos la matriz adjunta 
	simplmente se transpone la matriz de cofactores
	Finalmente, se halla 1/|A| y se multiplica por la matriz adjunta.

	
    '''
    return (1/np.linalg.det(A)*adjunct(A))  


rows = int(input("ingrese el tamaño de la matriz: "))
matrix = []
print("ingrese la matriz %s x %s: "% (rows, rows))
for i in range(rows):
    matrix.append(list(map(int, input().rstrip().split())))

Aarry=np.array(matrix)

myAinv=inverse(Aarry)
print("my A inverse:\n",myAinv,"\n")

Ainv=np.linalg.inv(Aarry)
# Tambien se genera una matríz inversa utilizando unicamente la libreria de Numpy
print("numpy A inverse:\n",Ainv)