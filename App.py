from collections import deque

q = deque([1 , 2 ,3 ])
q.append(4)
print(q.popleft())
print(q)

#! Top A Good Code

queue = [1, 2, 3]
queue.append(4)
queue.append(5)

print(queue.pop(0)) 
print(queue)

#! Top A bad code , For Bad Performance In Big Lists