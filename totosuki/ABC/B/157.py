A = [list(map(int, input().split())) for _ in range(3)]
rslt = [[False] * 3 for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]
answer = "No"

for i in range(N):
  for j in range(3):
    for k in range(3):
      if B[i] == A[j][k]:
        rslt[j][k] = True

bingo = [[[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]], [[2,0],[2,1],[2,2]],
         [[0,0],[1,0],[2,0]], [[0,1],[1,1],[2,1]], [[0,2],[1,2],[2,2]],
         [[0,0],[1,1],[2,2]], [[0,2],[1,1],[2,0]]]

for i in range(len(bingo)):
  for j in range(3):
    row = bingo[i][j][0]
    col = bingo[i][j][1]
    if rslt[row][col] == False:
      break
  else:
    answer = "Yes"

print(answer)