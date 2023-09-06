N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

for i in range(N):
  for j in range(i+1, N):
    x1, y1 = data[i]
    x2, y2 = data[j]
    x_diff = x2 - x1
    y_diff = y2 - y1
    rslt = y_diff / x_diff
    if -1 <= rslt <= 1:
      cnt += 1

print(cnt)