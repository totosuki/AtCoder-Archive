import sys
input = sys.stdin.buffer.readline

H, W = map(int, input().split())
S = [input().decode().strip() for _ in range(H)]

x1 = x2 = y1 = y2 = 0

for row in range(H):
  for col in range(W):
    if not x1 and S[row][col] == "o":
      x1 = col + 1
      y1 = row + 1
    elif x1 and S[row][col] == "o":
      x2 = col + 1
      y2 = row + 1

print(abs(x1-x2) + abs(y1-y2))