import sys
input = sys.stdin.buffer.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))
answer = "Yes"

for i in range(N):
  if i % 2:
    X -= A[i] - 1
  else:
    X -= A[i]
  
  if X < 0:
    answer = "No"

print(answer)