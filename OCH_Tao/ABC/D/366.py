N = int(input())
A = [[] for i in range(N)]
for i in range(N):
  for j in range(N):
    A[i].append(list(map(int,input().split())))
Q = int(input())
for i in range(Q):
  LX,RX,LY,RY,LZ,RZ = map(int,input().split())
  cnt=0
  for x in range(LX-1,RX):
    for y in range(LY-1,RY):
      for z in range(LZ-1,RZ):
        cnt+=A[x][y][z]
  print(cnt)