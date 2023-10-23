N = int(input())
data = []

for _ in range(N):
  T, D = map(int, input().split())
  data.append((T, T + D))

data.sort(key = lambda x: (x[1], x[0]))
time = 0
cnt = 0

for item in data:
  start, fin = item
  if time <= start:
    cnt += 1
    time = start + 1
  elif time <= fin:
    cnt += 1
    time += 1
  else:
    continue

print(cnt)

# [0 0 0 0 0 0]
# [0 0 0 0 0 0]
# [0 0 0 0 0 0]
# [0 0 0 0 0 0]
# [0 0 0 0 0 0]
# [0 0 0 0 0 0]