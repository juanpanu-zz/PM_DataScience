import numpy as np

def transponer(mat):
    t=[]                #New Array
    # iterate through rows
    for i in range(len(mat[0])):
        t.append([])
    # iterate through columns
        for j in range(len(mat)):
            t[i].append(mat[j][i])
    return t


X = [[12,7,10],           #Entry Matrix
    [4 ,5,9],
    [3 ,8,5]]

print(f'Matriz X:\n')
for tup in [X[row] for row in range(len(X))]:
    print(tup, end='\n' )
   
Xtr=transponer(X)

print(f'\nMatriz Transpuesta de X:\n')
for tup in [Xtr[row] for row in range(len(Xtr))]:
    print(tup, end='\n' )


"------------------------USANDO NUMPY-------------------------------"
Y= np.array(X)
Ytr=np.transpose(Y)
print(f'\nTranspuesta usando Numpy:\n\n{Ytr}')