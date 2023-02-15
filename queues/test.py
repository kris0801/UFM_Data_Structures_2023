'''
from queue import LinearQueue


# Queue instance
queue = LinearQueue(5)
print(queue)

# Enqueues
queue.enqueue('A')
print(queue)
queue.enqueue('B')
print(queue)
queue.enqueue('C')
print(queue)
queue.enqueue('D')
print(queue)
queue.enqueue('E')
print(queue)
queue.enqueue('F') # Queue Overflow
queue.enqueue('G') # Queue Overflow

# Dequeues
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue() # Queue Underflow (2nd scenario)
queue.dequeue() # Queue Underflow (2nd scenario)

queue_2 = LinearQueue(5)
print(queue_2)
queue.dequeue() # Queue Underflow (1st scenario)
'''


from tarea import Search
key = Search()
key.agregar("a", 1)
key.agregar("b", 2)
valor_a = key.buscar("a")
valor_c = key.buscar("c")
print(valor_a)  # imprime 1
print(valor_c)  # imprime None
'''

'''
from tarea import Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())  
print(stack.pop())  
print(stack.peek())  
print(stack.pop())   
print(stack.peek())  
print(stack.pop())   
print(stack.is_empty())  
'''
'''
from tarea import CircularQueue
q = CircularQueue(5)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.enqueue(6))  

print(q.dequeue())  
print(q.dequeue())  

q.enqueue(6)
q.enqueue(7)
q.enqueue(8)

print(q.dequeue())  
print(q.dequeue())
print(q.dequeue()) 
print(q.dequeue())  
print(q.dequeue())  
print(q.dequeue())
print(q.dequeue())