import sys
input = sys.stdin.buffer.readline

N = int(input())
A = [list(input().decode().rstrip()) for _ in range(N)]
answer = "correct"

for i in range(N):
  for j in range(N):
    if (A[i][j] == "W" or A[i][j] == "L") and (A[i][j] == A[j][i]):
      answer = "incorrect"
    elif A[i][j] == "D" and A[j][i] != "D":
      answer = "incorrect"

print(answer)