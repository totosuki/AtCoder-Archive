import sys
input = sys.stdin.buffer.readline

S, T = map(int, input().split())
A = list()
B = list()
C = list()
cnt = 0

for a in range(S+1):
  for b in range(S+1):
    for c in range(S+1):
      if (a+b+c) <= S:
        A.append(a)
        B.append(b)
        C.append(c)

for a, b, c in zip(A, B, C):
  if (a*b*c) <= T:
    cnt += 1

print(cnt)