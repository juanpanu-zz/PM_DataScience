class Node: 
    '''
    Clase Base para los Nodos,
    se requiere principalmente:
    data que contiene el valor a almacenar en el nodo
    next contiene la referencia al siguiente nodo en la lista.

    '''
    def __init__(self,data):
        self.data=data
        self.next=None
    
    def __repr__(self):
        return self.data


class LinkedList: 
    '''
    Clase base para la linked list
    permite los soguientes metodos:
    agregar al inicio.
    agregar al final.
    agregar antes del nodo especificado.
    agregar despues del nodo especificado.
    remover el nodo especificado.
    '''
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
            
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node
    
    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)


if __name__ == "__main__":
    llist =LinkedList()
    print(llist)

    first_node= Node("Fundamentos de Mat Fisica")
    llist.head = first_node
    print(llist)

    second_node= Node("Matrices")
    third_node= Node("SCRUM")
    first_node.next=second_node
    second_node.next=third_node
    print(llist)

    #fourth_node = Node("Algoritmos")
    next_node = Node("Expresiones Regulares")
    third_node.next=next_node
    #fourth_node.next=fifth_node
    #sixth_node = Node("MongoDB")
    #fifth_node.next=sixth_node
    print(llist)

    llist.add_first(Node("PreWork"))
    print(llist)

    llist.add_last(Node("Docker"))
    print(llist)

    llist.add_before("Expresiones Regulares",Node("MongoDB"))
    print(llist)

    llist.add_after("SCRUM", Node("Algoritmos"))
    print(llist)

    llist.remove_node("PreWork")
    print(llist)