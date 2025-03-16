from collections import deque

class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

    def __str__(self):
        return str(self.stack)

class Queue():
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None

    def __str__(self):
        return str(self.queue)

    def get_size(self):
        return len(self.queue)

characters = Stack()
characters.push("Ryu")
characters.push("Ken")
print(characters)
print(characters.pop())
print(characters.peek())
print(characters.pop())
print(characters.pop())

my_queue = Queue()
my_queue.enqueue(5)
my_queue.enqueue(10)
print(my_queue)
print(my_queue.dequeue())
print(my_queue.get_size())
