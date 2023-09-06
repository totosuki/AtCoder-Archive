import sys
input = sys.stdin.buffer.readline

N = int(input())
diff = 2025 - N
rslt = list()

for x in range(1, 10):
  for y in range(1, 10):
    if (x*y) == diff:
      rslt.append([x, y])

[print(f"{r[0]} x {r[1]}") for r in rslt]