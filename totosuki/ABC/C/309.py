import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
data = []
sm = 0
for _ in range(N):
  a, b = map(int, input().split())
  sm += b
  data.append([a, b])

data.sort()

if sm <= K:
  print(1)
else:
  for d in data:
    day = d[0]
    sm -= d[1]
    if sm <= K:
      print(day+1)
      break


# 累積和
B = [0] * (10**9+10)
sm = 0

for i in range(N):
  a, b = map(int, input().split())
  B[a] += b
  sm += b

cum = [sm] + [0] * (10**9+9)
if sm <= K:
  print(1)
else:
  for i in range(1, 10**9+9):
    cum[i] = cum[i-1] - B[i]
    if cum[i] <= K:
      print(i+1)
      break

# K錠以下になった日を出力
