import sys
input = sys.stdin.buffer.readline

N, X, Y = map(int, input().split())
R = 1
B = 0

for i in range(1, N):
  B += R*X
  R += B
  B += B*Y - B

print(B)