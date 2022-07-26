from Node import *

class LinkedList:
    def __init__(self, value=None):
        self.__head = Node(value)
    
    def __str__(self):
        lst = "<head> "
        currentHead = self.__head
        while currentHead != None:
            lst += (str)(currentHead.value) + " "
            currentHead = currentHead.next_node
        lst += "<tail>"
        
        return str(lst)
    
    @property
    def head(self):
        if self.__head == None:
            return None
        return self.__head.value
    
    @head.setter #add to head
    def head(self, value):
        if self.__head.value == None:
            self.__head = Node(value)
        else:
            currentHead = self.__head
            self.__head = Node(value)
            self.__head.next_node = currentHead
    
    @property
    def tail(self):
        if self.__head == None:
            return None
        currentHead = self.__head
        while currentHead.next_node != None:
            currentHead = currentHead.next_node
        
        return currentHead
    
    @tail.setter #add to tail
    def tail(self, value):
        if self.__head == None:
            self.__head = Node(value)
        currentHead = self.__head
        while currentHead.next_node != None:
            currentHead = currentHead.next_node
        currentHead.next_node = Node(value)
        
    def remove_head(self):
        if self.__head != None:
            print("Removed", self.__head)
            self.__head = self.__head.next_node
    
    def remove_tail(self):
        if self.__head != None:
            currentHead = self.__head
            while currentHead.next_node.next_node != None:
                currentHead = currentHead.next_node
            print("Removed", currentHead.next_node)
            currentHead.next_node = None
            
    
    
            

if __name__ == "__main__":
    lnklst = LinkedList()
    lnklst.head = "Anthony"
    lnklst.head = "Bianca"
    lnklst.tail = "Chris"
    lnklst.tail = "Diamond"
    lnklst.tail = "Emily"
    lnklst.tail = "Fred"
    print(lnklst)
    lnklst.remove_tail()
    print(lnklst)
    lnklst.remove_head()
    print(lnklst)
