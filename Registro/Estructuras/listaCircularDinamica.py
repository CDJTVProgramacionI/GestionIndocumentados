class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

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

    def search(self, data):
        if not self.head:
            return False
        temp = self.head
        while True:
            if temp.data == data:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

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