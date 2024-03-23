class Node:
    def __init__(self, data):
        self.data = data;
        self.previous = None;
        self.next = None;

class DoublyLinkedList:
    def __init__(self):
        self.head = None;
        self.tail = None;

    def addNode(self, data):
        newNode = Node(data);

        if(self.head == None):
            self.head = self.tail = newNode;
            self.head.previous = None;
            self.tail.next = None;
        else:
            self.tail.next = newNode;
            newNode.previous = self.tail;
            self.tail = newNode; 
            self.tail.next = None;

