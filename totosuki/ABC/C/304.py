import sys, collections, math
input = sys.stdin.buffer.readline

N, D = map(int, input().split())
data = []
for _ in range(N):
  X, Y = map(int, input().split())
  data.append([X, Y])

status = [False] * N
status[0] = True

queue = collections.deque([data.pop(0)])

while len(queue):
  x, y = queue.popleft()

  for i in range(len(data)):
    nx, ny = data[i]
    dist = math.sqrt((x-nx)**2 + (y-ny)**2)
    if (dist <= D) and (status[i] == False):
      status[i] = True
      queue.append(data.pop(i))

for i in range(N):
  print("Yes") if status[i] else print("No")