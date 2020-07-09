class Node: 
    '''
    Clase Base para los Nodos,
    se requiere principalmente:
    data que contiene el valor a almacenar en el nodo
    next contiene la referencia al siguiente nodo en la lista.

    '''
    def __init__(self,data=None,next_node= None, prev_node = None):
        self.data=data
        self.next_node=next_node
        self.prev_node=prev_node
    
    def __repr__(self):
        return self.data


class DoublyLinkedList(object): 
    '''
    Clase base para la linked list
    permite los soguientes metodos:
    agregar al inicio.
    agregar al final.
    agregar antes del nodo especificado.
    agregar despues del nodo especificado.
    remover el nodo especificado.
    '''
    def __init__(self, head = None):
        self.head = head
     
    def traverse(self):
        #tomar el primer nodo
        curr_node = self.head

        #continua hasta que se alcance el final de la lista
        while curr_node != None:
            print(curr_node.data)
            # toma el nodo despues del antiguo "actual"
            curr_node=curr_node.next_node

    def get_list_size(self):
        #definir contador
        count=0
        #tomar el primer nodo
        curr_node = self.head

        #continua hasta que se alcance el final de la lista
        while curr_node != None:
            count = count+1
            # toma el nodo despues del antiguo "actual"
            curr_node=curr_node.next_node
            return count

    def insert_beg(self,data):
        
        # definir nuevo nodo
        new_node=Node(data)

        # nuevo nodo es la antigua cabeza
        new_node.next_node=self.head
        # dado que ahora es la cabeza, no apunta a nada como anterior
        new_node.prev_node=None

        #por si la lista no está vacia
        if self.head != None:
            self.head.prev_node=new_node

        #actualizar la cabeza
        self.head=new_node

    def insert_end(self, data):
        #Definir un nuevo nodo
        new_node= Node(data)

        #al final de la lista para que el siguiente apuntador, apunte a nada   
        new_node.next_node= None
        
        if self.head== None:
            new_node.prev_node=None
            self.head= new_node

        #se toma el primer nodo
        first_node= self.head

        #ir al final de la lista
        while first_node.next_node:
            first_node= first_node.next_node

        #siguiente nodo igual al nuevo node.
        first_node.next_node= new_node
        new_node.prev_node = first_node

    def insert_before(self,ref_node,data):

        if self.head is None:
            print('The list is empty')
            return

        #definir nuevo nodo
        new_node=Node(data)

        new_node.prev_node= ref_node.prev_node
        ref_node.prev_node= new_node
        new_node.next_node= ref_node

        if new_node.prev_node!=None:
            new_node.prev_node.next_node=new_node
        else:
            self.head=new_node

    def insert_after(self,ref_node,data):
        
        if self.head is None:
            print('The list is empty')
            return

        
        #definir nuevo nodo
        new_node=Node(data)

        new_node.next_node=ref_node.next_node
        ref_node.next_node=new_node
        new_node.prev_node=ref_node

        if new_node.next_node != None:
            new_node.next_node.prev_node=new_node

    def delete_at_start(self):

        
        # En caso de lista vacia
        if self.head is None:
            print("The list has no element to delete")
            return 
        
        # en caso de que sea solo la cabeza
        if self.head.next_node is None:
            self.head = None
            return
        
        # se asigna la cabeza al nodo siguiente
        self.head = self.head.next_node
        
        # se asigna el nodo anterior de la cabeza a ninguno
        self.head.prev_node = None

    def delete_at_end(self):
 
        # caso vacio
        if self.head is None:
            print("The list has no element to delete")
            return
        
        # caso de solo cabeza
        if self.head.next_node is None:
            self.head = None
            return
        
        # tomo el primer nodo
        curr = self.head
        
        # recorro hasta encontrar el final.
        while curr.next_node is not None:
            curr = curr.next_node
        
        # tomo el nodo anterior apunto su siguiente nada 
        curr.prev_node.next_node = None

    def delete_element_by_value(self, x):        
        
        # en caso de lista vacia
        if self.head is None:
            print("The list has no element to delete")
            return
        
        # lista con solo cabeza
        if self.head.next_node is None:
            
            # verificar que el valor exista y si lo hace se limina el nodo
            if self.head.data == x:
                self.head = None
            else:
                print("Item not found")
            return 

        # en caso de que el valor sea el primero
        if self.head.data == x:
            self.head = self.head.next_node
            self.head.prev_node = None
            return

        # tomo el primer nodo
        n = self.head
        
        # recorro la lista
        while n.next_node is not None:

            #si el valor es encontrado
            if n.data == x:
                break
                
            # tomo el siguiente nodo
            n = n.next_node

        # en caos de encontrarlo en algun lugar de la lista.
        if n.next_node is not None:

            # tomo el nodo siguiente del anterior y lo asigno al siguiente nodo de despues del que coniente el valor
            n.prev_node.next_node = n.next_node
            # tomo el nodo anterior del siguiente y lo asigno al siguiente nodo de antes del que coniente el valor
            
            n.next_node.prev_node = n.prev_node

        else:

            # en cualquier otro caso el valor se encuentra al final.
            if n.data == x:
                # sse toma el nodo anterior, y se toma su siguiente nodo y se asigna a none.
                n.prev_node.next_node = None
            else:
                print("Element not found")

if __name__ == "__main__":

    # defino la lista
    double_list = DoublyLinkedList()

    # inserto valores al inicio
    double_list.insert_beg(90)
    double_list.insert_beg(90)
    double_list.insert_beg(90)
    double_list.insert_beg(80)
    double_list.insert_beg(70)

    print('-'*100)
    print('Despues de insertar')
    print('-'*100)
    double_list.traverse()

    # defino un nodo
    first_node = double_list.head

    # inserto despues de ese nodo
    double_list.insert_before(first_node, 50)

    print('-'*100)
    print('Insertar antes del primer nodo')
    print('-'*100)
    double_list.traverse()

    # inserto valor al final
    double_list.insert_end(100)

    # defino un nodo
    my_node = double_list.head.next_node

    # inserto valores despues de ese nodo
    double_list.insert_after(my_node, 60)
    double_list.insert_after(my_node, 80)

    # imprimo
    print('-'*100)
    print('Insertar al final y en el nodo especificado')
    print('-'*100)
    double_list.traverse()

    # delete the first value
    double_list.delete_at_start()

    print('-'*100)
    print('Despues de eliminar la cabeza')
    print('-'*100)
    double_list.traverse()

    # delete the last value
    double_list.delete_at_end()

    print('-'*100)
    print('Luego de eliminar la cola')
    print('-'*100)
    double_list.traverse()
        