N = int(input())
A = []
for i in range(N):
  A.append(list(input()))
B = []
for i in range(N):
  B.append(list(input()))
for i in range(N):
  for j in range(N):
    if A[i][j]!=B[i][j]:
      print(f"{i+1} {j+1}")
      break