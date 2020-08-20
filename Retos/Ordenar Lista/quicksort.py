#necesitamos dividir nuestro data set
#necesitamos el punto pivotal
#recursivamente ordenar cada mitad de mi array

def partition(arr, low, high):#creamos la particion del array
    i = (low-1) # i va a tomar el valor del indice mas bajo low-1
    pivot = arr[high] #valor medio de los datos, que separa los datos altos y bajos | dividimos el data set

    for j in range(low,high): #recorrer todo el rango de indices de low a high
        if arr[j] <= pivot: #de un lado se ponen todos los valores menores al pivot 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1] #de otro lado se ponen los valores mayores al pivot
    return (i+1)

def quickSort(arr, low, high):#creamos la funcion del quick sort
    if low < high: 
        pi = partition(arr, low, high)  #llamamos a la funcion partition
        quickSort(arr, low, pi-1)  #recursivamente usamos quicksort del low a la mitad(pi-1)
        quickSort(arr, pi+1, high) #recursivamente usamos quicksort en la otra mitad del (pi+1) al high

arr = [1991, 1990, 10, 5, 6, 0, 1, -10]
n = len (arr) #len nos da el tamaño del arreglo n=8
quickSort(arr, 0, n-1) #ejecutamos quickSort (arr, 0, 7)
print("Array Ordenado:") #imprimimos el arreglo
for i in range (n): 
    print("%d" %arr[i])