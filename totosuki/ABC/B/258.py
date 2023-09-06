import sys
input = sys.stdin.buffer.readline

N = int(input())
A = [list(map(int, input().decode().strip())) for _ in range(N)]
angle = [[-1,1], [0,1], [1,1],
         [-1,0],        [1,0],
         [-1,-1],[0,-1],[1,-1]]
max_num = 0
max_num_pos = []
rslt = []

# Get max num
for i in range(N):
  max_num = max(max_num, max(A[i]))

# Get max num pos
for i in range(N):
  for j in range(N):
    if A[i][j] == max_num:
      max_num_pos.append([i, j])

for pos in max_num_pos:
  for ag in angle:
    x,y = pos[0],pos[1]
    tmp = str(A[x][y])
    for _ in range(N-1):
      x = (x+ag[0]) % N
      y = (y+ag[1]) % N
      tmp += str(A[x][y])
    rslt.append(tmp)

print(max(rslt))