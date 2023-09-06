import time

st = time.time()
nt = time.time()

A, B, C, D = map(int, input().split())
blue = A+B
red = 0+C
cnt = 1

while nt - st <= 1.5:
  if (blue / red) <= D:
    print(cnt)
    exit()
  blue += B
  red += C
  cnt += 1
  nt = time.time()

print(-1)