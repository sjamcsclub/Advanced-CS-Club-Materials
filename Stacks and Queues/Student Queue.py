class Queue:
    # FIFO

    def __init__(self):
        self.items = []

    # def isEmpty(self):
    # code this method such that it returns a boolean when the stack is empty

    def enqueue(self, item):
        self.items.insert(0, item)

    # def dequeue(self):
    # code this so that it returns and removes the last entry from the Queue

    def size(self):
        return len(self.items)
