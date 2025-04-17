from collections import deque

fila = deque()

fila.append('a')
fila.appendleft('b')
print(fila)

fila.pop()
fila.popleft()
