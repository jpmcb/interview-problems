# John McBride
# June 26th 2018

# Question 3 - Seralize a binary tree

# Given the root to a binary tree, 
# implement serialize(root), which serializes the tree into a string, 
# and deserialize(s), which deserializes the string back into the tree.

# Given the following Node class, the following test should pass

# The binary tree class
class Node:
    # Constructor for the binary tree
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Prints out the binary tree
    def printTree(self):
        if(self.left):
            self.left.printTree()
        print(self.val)
        if(self.right):
            self.right.printTree()

    # Recursively builds the bin tree when inserting a node
    def addNode(self, inVal):
        if self.val:
            if(self.val >= inVal):
                if(self.left == None):
                    self.left = Node(inVal)
                else:
                    self.left.addNode(inVal)
            
            if(self.val < inVal):
                if(self.right == None):
                    self.right = Node(inVal)
                else:
                    self.right.addNode(inVal)

        else:
            self.val = inVal

    # Recursive method for serializing the tree values
    def serialHelper(self, arr):
        # Current node
        if(self.val):
            arr.append(self.val)
        else:
            arr.append(-1)
            
        # Go left
        if(self.left):
            self.left.serialHelper(arr)
        else:
            arr.append(-1)
            arr.append(-1)

        # Go right
        if(self.right):
            self.right.serialHelper(arr)
        else:
            arr.append(-1)
            arr.append(-1)
    
# Function called to sealize the tree using the helper method in the class
def serialize(root):
    serialArr = []
    root.serialHelper(serialArr)
    return serialArr

# Function toe deserialize the array returned by seralize
def deserialize(inArr):
    root = Node()
    for element in inArr:
        if(element != -1):
            root.addNode(element)

    return root


# -----
# Driver code
# -----
tree = Node("M")
tree.addNode("A")
tree.addNode("Z")
tree.addNode("B")
tree.addNode("X")

tree.printTree()

print(serialize(tree))
print(deserialize(serialize(tree)).printTree())