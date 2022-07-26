# Create the Node class below:
class Node:
    def __init__(self, value, next_node=None):
        self.__value = value
        self.__next_node = None
        
    def __str__(self):
         return str(self.__value)

    @property
    def value(self):
        return self.__value
    
    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, new_node):
        self.__next_node = new_node

#TESTING    
if (__name__ == "__main__"):
    P1 = Node("Anthony")
    P2 = Node("Bianca")
    P3 = Node("Chris")
    P4 = Node("Diamond")
    
    P1.next_node = P2
    P2.next_node = P3
    P3.next_node = P4
    
    
    
    
    currentNode = P1
    while (currentNode != None):
        print(currentNode)
        currentNode = currentNode.next_node    
    