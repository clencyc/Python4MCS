#create a node class to create a node
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

#create a linkedlist class
class LinkedList:
    def __init__(self):
        self.head = None

#insert node at the beginning
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node


#insert at the end of the list
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

        

#printing the linked list
    def printll(self):
        Current_node = self.head
        while Current_node:
            print(Current_node.data)
            Current_node = Current_node.next




llist = LinkedList()

llist.insertAtBegin('J')
llist.insertAtBegin('A')
llist.insertAtBegin('W')
llist.insertAtEnd('D')
llist.insertAtEnd('U')
llist.insertAtBegin('Q')
print("Node data was")
llist.printll() 