import numpy as np

X = [[12,7,10],             #Entry Matrix
    [4 ,5,9],
    [3 ,8,5]]

def transponer(mat):
    t=[]                #New Array
    # iterate through rows
    for i in range(len(mat[0])):
        t.append([])
    # iterate through columns
        for j in range(len(mat)):
            t[i].append(mat[j][i])
    return t

Xtr=transponer(X)
print(Xtr)
print(Xtr[1])
print(Xtr[2])


"------------------------USANDO NUMPY-------------------------------"
Y= np.array([[12,7,10],             #Entry Matrix
    [4 ,5,9],
    [3 ,8,5]])

Ytr=np.transpose(Y)

print(Ytr)