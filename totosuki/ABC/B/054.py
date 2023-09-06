N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

for i in range(N-M+1):
  for j in range(N-M+1):
    flag = False
    for k in range(M):
      for l in range(M):
        if A[k+i][l+j] != B[k][l]:
          flag = True
    if flag == False:
      print("Yes")
      exit()

print("No")