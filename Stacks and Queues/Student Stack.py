class Stack:
    # LIFO
    def __init__(self):
        self.items = []

    # def isEmpty(self):
    # code this method such that it returns a boolean when the stack is empty

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    # def peek(self):
    # return the last element

    def size(self):
        return len(self.items)
