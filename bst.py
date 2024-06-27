class Node:
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None


class BinarySearchTree:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if not self.head:
             self.head = Node(value)
        else:
            currentNode = self.head
            while True:
                if currentNode.value > value:
                    if not currentNode.left_child:
                        currentNode.left_child = Node(value)
                        print("to the left")
                        break
                    elif currentNode.left_child is not None:
                        currentNode = currentNode.left_child
                        continue
                elif currentNode.value < value:
                    if not currentNode.right_child:
                        currentNode.right_child = Node(value)
                        print("to the right")
                        break
                    elif currentNode.right_child is not None:
                         currentNode = currentNode.right_child
                         continue
                    
                    


    def fromArray(self, array):
        for int in array:
            BinarySearchTree.insert(self, int)

    def search(self, value):
        if not self.head:
            return False
        else:
            self.count = 1
            currentNode = self.head
            while True:
                if currentNode.value == value:
                    return True
                if currentNode.value > value:
                    if not currentNode.left_child:
                        return False
                    elif currentNode.left_child is not None:
                        currentNode = currentNode.left_child
                        self.count += 1
                        continue
                elif currentNode.value < value:
                    if not currentNode.right_child:
                        return False
                    elif currentNode.right_child is not None:
                         currentNode = currentNode.right_child
                         self.count += 1
                         continue




    def min(self):
        if not self.head:
            return None
        else:
            self.count = 1
            temp = self.head
            while temp.left_child:
                    temp = temp.left_child
                    self.count += 1
            return temp.value

    def max(self):
        if not self.head:
            return None
        else:
            self.count = 1
            temp = self.head
            while temp.right_child:
                    temp = temp.right_child
                    self.count += 1
            return temp.value

    def visitedNodes(self):
        return self.count