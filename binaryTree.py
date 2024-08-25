#creating a binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
class BinaryTree:
#Initialize the tree with a root node
    def __init__(self, root):
        self.root = Node(root)
    #Function to add a new value to the tree
    def addNode(self, currentNode, value):
        if value < currentNode.data:
            #we will start printing from left
            if currentNode.left is None:
                currentNode.left = Node(value)
            else:
                self.addNode(currentNode.left, value)
        else:
            #Now print from right
            if currentNode.right is None:
                currentNode.right = Node(value)
            else:
                self.addNode(currentNode.right, value)     
    def add(self, value):
        self.addNode(self.root, value)

    def in_order_traverse(self, Node, elements=[]):
        #left --> root --> right
        if Node:
            self.in_order_traverse(Node.left, elements)
            elements.append(Node.data)
            self.in_order_traverse(Node.right, elements)
        return elements
    
    def pre_order_traverse(self, Node, elements =[]):
         # Pre-order Traversal (root -> left -> right)
        if Node:
            elements.append(Node.data)
            self.pre_order_traverse(Node.left, elements)
            self.pre_order_traverse(Node.right, elements)
        return elements

        # Post-order Traversal (left -> right -> root)
    def post_order_traverse(self, Node, elements=[]):
        if node:
            self.post_order_traverse(Node.left, elements)
            self.post_order_traverse(Node.right, elements)
            elements.append(Node.data)
        return elements
        
        
if __name__ == "__main__":
    #create a Bianry Tree with root value of 10
    tree = BinaryTree(10)
    
    #add nodes to trhe binary tree
    elements = [6, 14, 3, 8, 12, 16]
    
    for element in elements:
        tree.add(element)
    # Perform in-order traversal
    print("In-order traversal:", tree.in_order_traverse(tree.root))
        