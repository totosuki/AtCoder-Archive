N = int(input())

for i in range(N+1):
  for j in range(N+1):
    for k in range(N+1):
      if i + j + k <= N:
        print(i, j, k)