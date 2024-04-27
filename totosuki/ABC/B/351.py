N = int(input())
tilea = [list(input()) for _ in range(N)]
tileb = [list(input()) for _ in range(N)]

for i in range(N):
  for j in range(N):
    if tilea[i][j] != tileb[i][j]:
      print(i+1,j+1)
      exit()