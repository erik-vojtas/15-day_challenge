class Node:
    def __init__(self, value):
        self.value = value
        self.next_value = None
        self.previous_value = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # def get_node(self, index):
    #     current = self.head
    #     for i in range(index):
    #         if current is None:
    #             return None
    #         current = current.next
    #     return current

    def insertAfter(self, node, new_node): # insert a node after a certain node
        new_node.previous_value = node
        if node.next_value is None:
            self.tail = new_node
        else:
            new_node.next_value = node.next_value
            new_node.next_value.previous_value = new_node
        node.next_value = new_node

    def insertBefore(self, node, new_node): # insert a node before a certain node
        new_node.next_value = node
        if node.previous_value is None:
            self.head = new_node
        else:
            new_node.previous_value = node.previous_value
            new_node.previous_value.next_value = new_node
        node.previous_value = new_node

    def insertAtStart(self, new_node): # insert a node with value at the start of the double linked list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.insertBefore(self.head, new_node)

    def insertAtEnd(self, new_node): # insert a node with value at the end of the double linked list
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.insertAfter(self.tail, new_node)

    def removeNode(self, node): # remove a node
        if node.previous_value is None:
            self.head = node.next_value
        else:
            node.previous_value.next_value = node.next_value
        if node.next_value is None:
            self.tail = node.previous_value
        else:
            node.next_value.previous_value = node.previous_value

    def printList(self): # display all item in the double linked list
        printed_value = self.head
        while printed_value:
            print(printed_value.value)
            printed_value = printed_value.next_value

    def deleteAll(self):  # delete all items in the double linked list
        self.head = None
        self.tail = None

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")

dl1 = DoubleLinkedList()

dl1.insertAtEnd(nodeD)
dl1.printList()
dl1.insertAtStart(nodeA)
dl1.printList()

dl1.insertAfter(nodeA, nodeB)
dl1.printList()

dl1.insertBefore(nodeD, nodeC)
dl1.printList()