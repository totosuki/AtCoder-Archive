N, K = map(int, input().split())
H = list(map(int, input().split()))
cnt = 0

for i in range(N):
  if H[i] >= K:
    cnt += 1

print(cnt)