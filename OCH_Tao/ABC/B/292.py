N, Q = map(int, input().split())
L = [0]*N
for i in range(Q):
  C, X = map(int, input().split())
  if C == 3:
    print("No" if L[X-1] < 2 else "Yes")
  else:
    L[X-1] += C
