import numpy as np
N = int(input())
A = []
for i in range(N):
  A.append(list(map(int, input().split())))
A = np.array(A)
B = []
for i in range(N):
  B.append(list(map(int, input().split())))
B = np.array(B)
for i in range(4):
  tmp=np.rot90(A,i)
  for x,y in np.ndindex(N,N):
    if tmp[x,y] and not B[x,y]:
      break
  else:
    print("Yes")
    break
else:
  print("No")