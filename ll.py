
class Node:
    data = 0
    next = None

    def __init__(self,data) -> None:
        self.data = data

def nodeCount(start_node):
    counter = 1
    current = start_node.next
    while current != None:
        current = current.next
        counter += 1
    return counter
A = Node(4)

B = Node(2)
A.next = B
C = Node(3)
B.next = C
D = Node(10)
C.next = D
print(nodeCount(A))