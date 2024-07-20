#We will understand the concept and implementation of a LinkedList in Python by first creating a Simple LinkedList and then a bit complex

# A LinkedList is a linear data structure where elements are not stored in contiguous memory locations. Instead, each element (called a node) contains data and a reference (link) to the next node in the sequence. This structure allows dynamic memory allocation and efficient insertion and deletion of elements.

#STEP - 1: CRETING A NODE CLASS
class Node:
    def __init__(self,data):
        self.classData = data
        self.nextNode = None
    #we created a class Node with two attributes:
    #ClassData: Which stores the data of the node
    #nextNode: Initially set to Nodne, as it points to the next Node (which for now doesn't exists)

#STEP - 2: CREATING A LINKEDLIST CLASS
class LinkedList:
    def __init__(self):
        self.head = None
    #we created a class LinkedList with one attribute: HEAD, which points to the first node of the LinkedList which is empty for now.

#STEP - 3: INSERTING a Node
def insert(self, data):
    newNode = Node(data)
    newNode.nextNode = self.head
    self.head = newNode
    #Insert methods adds a new node at the beginning of trhe LinkedList. It creates a new node with the given data.
    #Then, the nextNode of the new node is set to the current head of the LinkedList.
    #Finally, the head is updated to point to the new node.

#STEP - 4: PRINTING THE LINKEDLIST
def printList(self):
    temp = self.head
    while temp:
        print(temp.data, end= ' ')
        temp = temp.nextNode


#STEP - 5: COMPLETING THE LINKEDLIST AND PRINTING IT
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        newNode.next = self.head
        newNode.head = newNode

    def printList(self):
    temp = self.head
    while(temp):
        print(temp.data, end = ' ')
        temp = temp.next
    
# Create a linkedList    
linkedList = LinkedList()

# Insert some elements
linkedList.insert(1)
linkedList.insert(2)
linkedList.insert(3)

# Print the linkedList
linkedList.printList()




