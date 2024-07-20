class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def insert_at_beginning(self, data):
    newNode = Node(data)
    if self.head is None:
        self.head = newNode
        self.tail = newNode
    else:
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
 
def insert_at_end(self, data):
    newNode = Node(data)
    if self.head is None:
        self.head = newNode
        self.tail.newNode
    else:
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

def printList(self):
    temp = self.head
    while temp:
        print(temp.data, end= ' ')
        temp = temp.next

