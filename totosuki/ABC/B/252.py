import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = "No"

A_sorted = sorted(A, reverse = True)
for b in B:
  i = A[b-1]
  if A_sorted.index(i) == 0:
    answer = "Yes"

print(answer)