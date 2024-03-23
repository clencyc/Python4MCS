# dequeue 
#Step 1: Check if the queue is empty.
#Step 2: If the queue is empty, return the underflow error and exit.
#Step 3: If the queue is not empty, access the data where the front is pointing.
#Step 4: Increment the front pointer to point to the next available data element.
#Step 5: The Return success.

def dequeue(self):
    if self.isEmpty():
        raise Exception("Queue is empty")
        return
    else:
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.rear = None
        return data