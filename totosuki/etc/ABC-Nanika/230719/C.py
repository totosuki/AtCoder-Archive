import sys, time
st = time.perf_counter()
nt = time.perf_counter()
input = sys.stdin.buffer.readline

H, W = map(int, input().split())
G = [list(input().decode().strip()) for _ in range(H)]
x = 0
y = 0

while (nt - st) < 1.7:
  g = G[y][x]
  
  if g == "U" and y != 0:     y -= 1
  elif g == "D" and y != H-1: y += 1
  elif g == "L" and x != 0:   x -= 1
  elif g == "R" and x != W-1: x += 1
  else:
    print(y+1, x+1)
    exit()
  
  nt = time.perf_counter()

print(-1)