N, K = map(int, input().split())
cnt = 0
for i in range(1, N+1):
  for j in range(1, N+1):
    if 0 < K-(i+j) <= N:
      cnt += 1
print(cnt)
