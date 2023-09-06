import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
S = input().decode().strip().split()
T = set(input().decode().strip().split())

for s in S:
  if s in T:
    print("Yes")
  else:
    print("No")