N, M, C = map(int, input().split())
B = list(map(int, input().split()))
cnt = 0

for _ in range(N):
  tmp = C
  A = list(map(int, input().split()))
  
  for i in range(M):
    tmp += A[i] * B[i]

  if tmp > 0:
    cnt += 1

print(cnt)