from dataclasses import dataclass

class Node:
    data : any
    next: 'Node'
    prev: 'Node'
    
    def __init__(self, dato: any, siguiente: 'Node', anterior: 'Node'):
        self.data = dato
        self.next = siguiente
        self.prev = anterior
        
@dataclass
class DoubleLinkedList:
    __head : Node
    __len : int
    
    @property
    def len(self):
        return self.__len
    
    def __init__(self):
        self.__head = None
        self.__len = 0
        
    def insertAtBegin(self, dato: any):
        self.__head = Node(dato, self.__head, None)
        self.__len += 1
        
    def insertAtEnd(self, dato: any):
        if self.__head is None:
            self.__head = Node(dato, None, None)
        else:
            current = self.__head
            while current.next is not None:
                current = current.next
                
            current.next = Node(dato, None, current)
            
        self.__len += 1
        
    def insertAt(self, data : any, index : int):
        if index < 0 or index > self.__len:
            raise IndexError("Índice fuera de rango")
        
        if index == 0:
            self.insertAtBegin(data)
        else:
            current = self.__head
            for i in range(1, index):
                current = current.next
                
            current.next = Node(data, current.next, current)
            self.__len += 1
            
    def deleteAtBegin(self) -> any:
        if self.__head is None:
            raise IndexError("Lista vacía")
        
        val = self.__head.data
        self.__head = self.__head.next
        self.__len -= 1

        return val
    
    def deleteAtEnd(self) -> any:
        if self.__head is None:
            raise IndexError("Lista vacía")
        
        current = self.__head
        while current.next is not None:
            current = current.next
            
        val = current.data
        current.prev.next = None
        self.__len -= 1
        
        return val
    
    def deleteAt(self, index : int) -> any:
        if index < 0 or index >= self.__len:
            raise IndexError("Índice fuera de rango")
        
        if index == 0:
            return self.deleteAtBegin()
        
        current = self.__head
        for i in range(1, index):
            current = current.next
            
        val = current.next.data
        current.next = current.next.next
        self.__len -= 1
        
        return val
    
    def search(self, data : any) -> int:
        current = self.__head
        i = 0
        while current is not None:
            if current.data == data:
                return i
            current = current.next
            i += 1
            
        return -1
        
    
    def print(self):
        current = self.__head
        while current is not None:
            print(current.data)
            current = current.next

if __name__ == "main":
    lista = DoubleLinkedList()    