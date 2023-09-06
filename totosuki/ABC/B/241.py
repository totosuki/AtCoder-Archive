import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = "Yes"

for b in B:
  if b in A:
    A.remove(b)
  else:
    answer = "No"

print(answer)