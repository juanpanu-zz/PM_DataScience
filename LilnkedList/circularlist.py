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

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ".join(nodes))

if __name__ == "__main__":
    circular_llist = CircularLinkedList()
    circular_llist.print_list()

    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
    d.next = a
    circular_llist.head = a
    circular_llist.print_list()
    circular_llist.print_list(b)
    circular_llist.print_list(d)