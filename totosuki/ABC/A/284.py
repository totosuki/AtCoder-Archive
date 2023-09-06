N = int(input())
S = []
for _ in range(N):
  S.append(input())
for i in range(N):
  print(S[-i-1])