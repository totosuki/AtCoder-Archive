import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().split())

while not K <= 0:
  if N % 200 == 0:
    N //= 200
  else:
    N = int(str(N) + "200")
  K -= 1

print(N)