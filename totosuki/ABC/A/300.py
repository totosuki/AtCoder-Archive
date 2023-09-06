N, A, B = map(int, input().split())
C = list(map(int, input().split()))
result = A + B
for i, n in enumerate(C):
  if n == result:
    print(i + 1)