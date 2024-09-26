class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
           self.root = newNode
           return
        else:
            # Start at the root
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left == None:
                        current_node.left = newNode
                        return
                    current_node = current_node.left
                else:
                    if current_node.right == None:
                        current_node.right = newNode
                        return
                    current_node = current_node.right


    def lookup(self, value):
        if self.root is None:
            return None
        else:
            current_node = self.root
            while current_node is not None:
                if value < current_node.value:
                    current_node = current_node.left
                elif value > current_node.value:
                    current_node = current_node.right
                else:
                    return current_node
            return None


# Testing the BinarySearchTree
tree = BinarySearchTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(13)
tree.insert(18)
