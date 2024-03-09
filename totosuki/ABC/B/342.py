N = int(input())
P = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
  A, B = map(int, input().split())
  a = P.index(A)
  b = P.index(B)
  if (a < b):
    print(A)
  else:
    print(B)