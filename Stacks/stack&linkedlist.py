# implement stacks using singly linked lists.
# getSize()– Get the number of items in the stack.
# isEmpty() – Return True if the stack is empty, False otherwise.
# peek() – Return the top item in the stack. If the stack is empty, raise an exception.
# push(value) – Push a value into the head of the stack.
# pop() – Remove and return a value in the head of the stack. If the stack is empty, raise an exception.
# Node class is a building block for the stack class
# __str__ - provides a string representation of the stack for printing
# the stack class represents stack data structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    #here we initialize a stack using a dummy node.
    def __init__(self):
        self.head = Node("head") # used as a placeholder, it represents the top of the stack
        self.size = 0 # this keeps track of the number of elements in the stack

    # the string rep of the stack
    def __str__(self):
        current = self.head.next
        out = ""
        while current != None:
            out += str(current.value) + "->"
            current = current.next
        return out[:-6]

    # get the current size of the stack
    def getSize(self):
        return self.size

    # check if the stack is empty
    def isEmpty(self):
        return self.size is None # will return true if the stack is empty

    # get the top item of the stack
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.head.value

    # Push a value into the stack
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head # this inserts the new node at the top of the stack
        self.head = newNode # this makes the new node the top of the stack
        self.size += 1  # size of stack is increamented by

    # remove a value from the stack and return the stack
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value
    
    # main code

stack = Stack()
for i in range(1, 11):
        stack.push(i)
print(f"Stack: {stack}")
print(f"Stack size: {stack.getSize()}")
print(f"Stack is empty: {stack.isEmpty()}")
print(f"Stack top: {stack.peek()}")
print(f"Stack before pop: {stack}")
stack.pop()
print(f"Stack after 1st pop : {stack}")
stack.pop()
print(f"Stack after 2nd pop : {stack}")
stack.pop()
print(f"Stack after 3rd pop : {stack}")
print(f"Stack: {stack}")
print(f"Stack size: {stack.getSize()}")
print(f"Stack is empty: {stack.isEmpty()}")
print(f"Stack top: {stack.peek()}")
