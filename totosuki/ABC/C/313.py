import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
sm = sum(A)
X = sm // N
R = sm % N
rslt = 0

A.sort(reverse = True)

for a in A:
  if R > 0:
    R -= 1
    rslt += abs(a - (X+1))
  else:
    rslt += abs(a - X)

print(rslt//2)