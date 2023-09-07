import numpy as np

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

answer = "No"

for _ in range(4):
  flag = True
  for row in range(N):
    for col in range(N):
      if A[row][col] and not B[row][col]:
        flag = False
  
  if flag:
    answer = "Yes"

  A = list(np.rot90(A))

print(answer)