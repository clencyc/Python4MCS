# this is the Enqueue algorithm
#Step 1: Check if the queue is full.
#Step 2: If the queue is full, return overflow error and exit.
#Step 3: If the queue is not full, increment the rear pointer to point to the next empty space.
#Step 4: Add the data element to the queue location, where the rear is pointing.
#Step 5: return success.

def Enqueue(queue, rear, size, data):
    if rear == size:
        print("Queue is full")
    else:
        queue.append(data)
        rear += 1
    return rear - 1