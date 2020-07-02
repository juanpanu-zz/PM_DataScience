SIZE=5
VALUES=[None]*SIZE
HEAD=-1
TAIL=-1

def enQueue(value:int):
    global HEAD
    global TAIL
    global VALUES
    if(TAIL == SIZE-1):
        print("Nuestro Queue esta lleno\n" )
    else:
        if(HEAD==-1):
            HEAD = 0
        TAIL+=1
        VALUES[TAIL]=value
        print(f"Se inserto el valor {value} correctamente\n")

def deQueue():
    global HEAD
    global TAIL
    global VALUES
    if(HEAD == -1):
        print("Nuestro Queue esta vacio\n" )
    else:
        print(f"se elimino el valor {VALUES[HEAD]}\n")
        HEAD+=1
        if(HEAD > TAIL):
            HEAD = TAIL = -1



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