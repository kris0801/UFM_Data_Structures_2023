class Search:
    def _init_(self):
        self.datos = {}

    def agregar(self, key, valor):
        self.datos[key] = valor

    def buscar(self, key):
        if key in self.datos:
            return self.datos[key]
        else:
            return None
        
    
class Stack:
    def _init_(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
class CircularQueue:
    def _init_(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail and not self.queue[self.head]

    def is_full(self):
        return self.head == self.tail and self.queue[self.head]

    def enqueue(self, item):
        if self.is_full():
            return "La cola está llena"
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.k

    def dequeue(self):
        if self.is_empty():
            return "La cola está vacía"
        temp = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.k
        return temp