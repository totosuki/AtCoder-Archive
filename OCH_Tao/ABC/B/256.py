from collections import deque
N = int(input())
A = list(map(int,input().split()))
X = deque([0]*4)
cnt = 0
for i in A:
  X[0]=1
  for j in range(i):
    cnt+=X.pop()
    X.appendleft(0)
print(cnt)