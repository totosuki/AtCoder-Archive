import sys
input = sys.stdin.buffer.readline

N, S, D = map(int, input().split())
answer = "No"

for i in range(N):
  X, Y = map(int, input().split())
  if X < S and Y > D:
    answer = "Yes"

print(answer)