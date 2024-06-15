N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 0

j = 0 # N
for i in range(M):

  while j < N and A[j] < B[i]:
    j += 1
  
  if j == N:
    print(-1)
    exit()
  
  ans += A[j]
  j += 1

print(ans)