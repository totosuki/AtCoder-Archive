import sys
input = sys.stdin.buffer.readline

A, B = map(int, input().split())
SM = str(A + B)
A = str(A).zfill(len(SM))
answer = "Easy"

for sm, a in zip(SM, A):
  if sm < a:
    answer = "Hard"

print(answer)