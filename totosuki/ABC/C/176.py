import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
sm = 0
tall = 0

for i in range(N):
  if tall <= A[i]:
    tall = A[i]
  else:
    sm += tall - A[i]

print(sm)