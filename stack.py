from collections import deque

stack = deque()

stack.append('Task1')
stack.append('Task2')
stack.append('Task3')

print(stack)

stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)