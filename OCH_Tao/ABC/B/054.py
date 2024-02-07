N,M = map(int,input().split())
A = []
B = []
for i in range(N):
  A.append(input())
for i in range(M):
  B.append(input())
for i in range(N-M+1):
  if B[0] in A[i]:
    x = A[i].find(B[0])
    for j in range(1,M):
      if (A[i+j])[x:x+M] != B[j]:
        break
    else:
      print("Yes")
      break
else:
  print("No")