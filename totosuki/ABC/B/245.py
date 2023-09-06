import sys
input = sys.stdin.buffer.readline

N = int(input())
A = set(map(int, input().split()))

for i in range(N+1):
  if not i in A:
    print(i)
    break