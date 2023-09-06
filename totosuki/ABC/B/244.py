import sys
input = sys.stdin.buffer.readline

N = int(input())
T = input().decode().strip()
pos = [0, 0]
angle = 0

for t in T:
  if t == "S":
    if angle == 0:
      pos[0] += 1
    elif angle == 90:
      pos[1] -= 1
    elif angle == 180:
      pos[0] -= 1
    elif angle == 270:
      pos[1] += 1
  else:
    angle = (angle + 90) % 360

print(*pos)