import sys
input = sys.stdin.buffer.readline

K = int(input())
mod = 10000000019
X = 7

for i in range(K):
  if (X := X % K) == 0:
    print(i+1)
    break
  else:
    X = X * 10 + 7
else:
  print(-1)
