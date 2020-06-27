def producto(MatrixA,MatrixB):
    '''Realiza el producto maticial, inicialmente verifica que
        el numero de columnas en la matriz A sea igual
        al numero de filas en la matriz B
        
        El elemento cij de la matriz producto se obtiene multiplicando cada elemento de la fila i de la matriz
        A por cada elemento de la columna j de la matriz B y sumándolos
        '''
    rowsA = len(MatrixA)
    colsA = len(MatrixA[0])
    rowsB = len(MatrixB)
    colsB = len(MatrixB[0])
    
    C=[] 
    
    if colsA==rowsB:
        print(f'La matriz A :')
        for tup in [MatrixA[row] for row in range(rowsA)]:
            print(tup, end='\n' )
        print(f'\ny la matriz B :')
        for tup in [MatrixB[row] for row in range(rowsB)]:
            print(tup, end='\n' )
        print(f'\nSon multipicables, el resultado es \nC = A*B :')
        # Iteracion en las filas de A
        for i in range(rowsA):
            C.append([])
            # Iteracion en las columnas de B
            for j in range(colsB):
                C[i].append([])
                cijelement=0    #En cada cambio de posición reinicio el contador
                # Iteracion en las filas de B 
                for k in range(rowsB):
                    C[i][j] = 0 #inicio en 0 la posicion de la matriz C
                    cijelement+=MatrixA[i][k]*MatrixB[k][j]
                    C[i][j] += cijelement   
        return C
    else:
        print('Las matrices ingresadas no son multiplicables')

A=[[2,0,1],             #Matrix A
   [3,0,0],
   [5,1,1]]

B=[[1,0,1],             #Matrix B
   [1,2,1],
   [1,1,0]]

C=producto(A,B)
for row in range(len(C)):
    print(C[row])