import sys
input = sys.stdin.buffer.readline

N = int(input())
A = map(int, input().split())
rslt = int()

for a in A:
  if a > 10:
    rslt += a - 10

print(rslt)