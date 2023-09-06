N = int(input())
A = list(map(int, input().split()))
A.sort()

for i in range(N-1):
  if A[i]+1 == A[i+1]:
    continue
  else:
    print(A[i]+1)
    break