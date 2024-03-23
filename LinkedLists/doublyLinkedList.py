# implementing circular linked lists
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        # itr traverses the list 
        itr = self.head
        # llstr initializes an empty string
        llstr = ''
        while itr != None:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    # take values as input and create a new linked list
    def insert_values(self, data_list):
        self.home = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count
    
    def remove_at(self, index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")

        if index==0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr != None:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next

            count += 1
        
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")

        if index==0:
            self.insert_at_beginning(data)

            return
        count = 0
        itr = self.head
        while itr != None:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    # inserting elements after a certain value in the linked list
    def insert_after_value(self, data_after, data_to_insert):
            if self.head is None:
                return
            if self.head.data == data_after:
                self.head.next = Node(data_to_insert, self.head.next)
                return
            itr = self.head
            while itr:
                if itr.data == data_after:                        
                    itr.next = Node(data_to_insert, itr.next)
                break
                itr = itr.next



ll = Linkedlist()
ll.insert_at_beginning(5)
ll.print()
ll.insert_at_beginning(89)
ll.print()
ll.insert_at_beginning(6)
ll.print()
ll.insert_at_beginning(7)
ll.print()
ll.insert_at_end(256)
ll.print()
ll.insert_at_end(2345)
ll.print()
ll.insert_values(["banana", "mango", "grapes", "orange"])
ll.print()
print("Length of linked list: ", ll.get_length())
ll.remove_at(3)
ll.print()
ll.insert_at(3, "figs")
ll.print()
ll.insert_after_value("Banana", "True")
ll.print()