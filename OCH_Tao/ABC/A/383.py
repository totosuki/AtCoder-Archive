N = int(input())
cnt = 0
time = 0
for i in range(N):
  T, V = map(int, input().split())
  cnt = max(0, cnt-(T-time))
  time = T
  cnt += V
print(cnt)
