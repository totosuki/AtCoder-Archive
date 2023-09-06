N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
rslt = 0
for b in B:
  rslt += A[b - 1]
print(rslt)