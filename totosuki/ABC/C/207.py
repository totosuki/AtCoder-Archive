import sys
input = sys.stdin.buffer.readline

N = int(input())
data = []
cnt = 0

for _ in range(N):
  t, l, r = map(int, input().split())

  if t == 2: r -= 0.2
  if t == 3: l += 0.2
  if t == 4:
    r -= 0.2
    l += 0.2
  
  data.append([l, r])

for i in range(N):
  for j in range(i+1, N):
    l1, r1 = data[i]
    l2, r2 = data[j]
    
    if max(l1, l2) <= min(r1, r2):
      cnt += 1

print(cnt)