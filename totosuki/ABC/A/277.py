N, X = map(int, input().split())
P = list(map(int, input().split()))
for i, p in enumerate(P):
  if p == X:
    print(i + 1)