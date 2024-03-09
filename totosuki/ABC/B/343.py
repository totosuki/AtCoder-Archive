N = int(input())

for i in range(N):
  L = list(map(int, input().split()))
  for j in range(N):
    if L[j] == 1:
      print(j+1, end = " ")
  print()