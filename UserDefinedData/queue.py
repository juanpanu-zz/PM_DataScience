"""
1 - Crear pointer para saber que hay en front y rear
2 - colocar estos valores en -1 al inicializar
3 - incrementar en 1 el valor de "rear"
    cuando agreguemos un elemento
4 - Retornar el valor de front al quitar un elemento 
    e incrementar en 1 el valor de
    front al usar dequeue,
5.- antes de agregar un elemento revisar si hay espacio
6.- antes de remover un elemento revisamos que existan elementos
7.- asegurarnos de que al remover todos los elementos 
    resetear nuestro front y rear a -1 
    y agregar el valor de 0 a Front al hacer nuestro primer enqueue 

 """
SIZE=5
VALUES=[None]*SIZE
FRONT=-1
REAR=-1

def enQueue(value:int):
    global FRONT
    global REAR
    global VALUES
    if(REAR == SIZE-1):
        print("Nuestro Queue esta lleno\n" )
    else:
        if(FRONT==-1):
            FRONT = 0
        REAR+=1
        VALUES[REAR]=value
        print(f"Se inserto el valor {value} correctamente\n")

def deQueue():
    global FRONT
    global REAR
    global VALUES
    if(FRONT == -1):
        print("Nuestro Queue esta vacio\n" )
    else:
        print(f"se elimino el valor {VALUES[FRONT]}\n")
        FRONT+=1
        if(FRONT > REAR):
            FRONT = REAR = -1



enQueue(10)
enQueue(22)
enQueue(13)
enQueue(44)
enQueue(56)
deQueue()
deQueue()
deQueue()
deQueue()
deQueue()
enQueue(10)