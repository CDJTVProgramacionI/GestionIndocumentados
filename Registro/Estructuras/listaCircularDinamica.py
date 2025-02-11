class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    __len = 0
    
    def __init__(self):
        self.head = None
        self.__len = 0
        
    def size(self):
        return self.__len
        

    def insertAtBegin(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node
            
        self.__len += 1

    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            
        self.__len

    def insertAt(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
            if temp == self.head:
                raise IndexError("Index out of bounds")
        new_node.next = temp.next
        temp.next = new_node
        
        self.__len += 1

    def deleteAtBegin(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
            
        self.__len -= 1

    def deleteAtEnd(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
            temp.next = self.head
            
        self.__len -= 1

    def deleteAt(self, index):
        if not self.head:
            return
        if index == 0:
            self.delete_at_beginning()
            return
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
            if temp.next == self.head:
                raise IndexError("Index out of bounds")
        temp.next = temp.next.next
        
        self.__len -= 1

    def search(self, data):
        index = -1
        if not self.head:
            return index
        temp = self.head
        while True:
            index += 1
            if temp.data == data:
                return index
            temp = temp.next
            if temp == self.head:
                break
        return -1

    def print(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print()