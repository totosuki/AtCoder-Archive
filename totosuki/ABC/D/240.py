import sys; from collections import deque
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
queue = deque([])
top = 0
cnt = 0

for a in A:
  if top != a:
    top = a
    queue.append([top, 1])
  else:
    queue[-1][1] += 1
  
  cnt += 1
  
  if queue[-1][0] == queue[-1][1]:
    trash = queue.pop()
    cnt -= trash[1]
    if queue:
      top = queue[-1][0]
    else:
      top = 0
  
  print(cnt)




# top = 0
# cnt = 1
# queue = deque()

# for a in A:
#   if top != a:
#     cnt = 1
#     top = a
#   else:
#     cnt += 1
  
#   queue.append(a)
  
#   if top == cnt:
#     while cnt > 0:
#       _ = queue.pop()
#       cnt -= 1
    
#     if queue:
#       top = queue[-1]
#     else:
#       top = 0
#     cnt = 1

#   if queue:
#     print(len(queue))
#   else:
#     print(0)

# 数値にする必要がある [a, cnt]