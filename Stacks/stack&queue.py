#this implements a stack using a queue
from collections import deque
from typing import Any
stack = deque()

stack.append("Infinix")
stack.append("Samsung")
stack.append("Nokia")
stack.append("I-Phone")
print(stack)
stack.pop()
print(stack)
