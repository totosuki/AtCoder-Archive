N = int(input())
for i in range(N+1):
  for j in range(N+1-i):
    for k in range(N+1-i-j):
      print(i,j,k)