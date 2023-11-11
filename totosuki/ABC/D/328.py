from collections import deque

S = input() # ABCのみ入る

q = deque()

for s in S:
  q.append(s)
  
  if len(q) < 3: continue
  
  while q[-3] == "A" and q[-2] == "B" and q[-1] == "C":
    q.pop()
    q.pop()
    q.pop()
    if len(q) < 3: break

print("".join(q))