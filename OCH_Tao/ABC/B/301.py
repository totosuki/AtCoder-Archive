N = int(input())
A = list(map(int, input().split()))
L = []
for i in range(N-1):
  if A[i] < A[i+1]:
    L.extend(list(range(A[i], A[i+1])))
  else:
    L.extend(list(range(A[i], A[i+1], -1)))
L.append(A[-1])
print(*L)
