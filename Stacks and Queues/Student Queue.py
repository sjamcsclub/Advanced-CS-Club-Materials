class Queue:
    """Stack class represents a first-in-first-out (FIFO) stack of objects"""

    def __init__(self):
        self.items = []

    # def isEmpty(self):
    # code this method such that it returns a boolean when the stack is empty

    def enqueue(self, item):
        self.items.insert(0, item)

    # def dequeue(self):
    # code this so that it returns and removes the first entry from the Queue
    # in this case it is the last element of the array

    def size(self):
        return len(self.items)
