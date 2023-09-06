import sys
input = sys.stdin.buffer.readline

N, W = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort(reverse = True)
rslt = 0

for d in data:
  A, B = d[0], d[1]
  
  if B > W:
    rslt += A * W
  else:
    rslt += A * B
  W -= B
  
  if W <= 0:
    break

print(rslt)