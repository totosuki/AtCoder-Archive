N = int(input())
A = list(map(int, input().split()))
L = set(range(1, N+1))
for i in range(N):
  if i+1 in L:
    L.discard(A[i])
print(len(L))
print(*sorted(L))
