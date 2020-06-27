Solución al reto de de Matrices.

Se encuentran 3 archivos:

1. Transpuesta.py 
	En este se define una función que se encarga de transponer una matriz A
	usando un ciclo for dentro de otro, generando así una matriz At donde sus
	posiciones corresponden a At[i][j] = A[j][i].
	
	Finalmente se muestra el resultado usando Numpy.

2.MatrizProducto.py
	Realiza el producto maticial, inicialmente verifica que
        el numero de columnas en la matriz A sea igual
        al numero de filas en la matriz B
        
        El elemento cij de la matriz producto se obtiene multiplicando cada elemento
	de la fila i de la matriz A por cada elemento de la columna j de la matriz B y sumándolos

3.MatrizInversa.py
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

	Tambien se genera una matríz inversa utilizando unicamente la libreria de Numpy.
	