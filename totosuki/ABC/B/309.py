import sys
input = sys.stdin.buffer.readline

N = int(input())
A = [list(map(int, input().decode().strip())) for _ in range(N)]
rslt_list = []

# ue
rslt = []
for i in range(N):
  if i == 0:
    rslt.append(A[1][0])
  else:
    rslt.append(A[0][i-1])
rslt_list.append(rslt)

# center
if N != 2:
  for i in range(1, N-1):
    rslt = []
    for j in range(N):
      if j == 0:
        rslt.append(A[i+1][j])
      elif j == N-1:
        rslt.append(A[i-1][j])
      else:
        rslt.append(A[i][j])
    rslt_list.append(rslt)

# sita
rslt = []
for i in range(N):
  if i == N-1:
    rslt.append(A[N-2][i])
  else:
    rslt.append(A[N-1][i+1])
rslt_list.append(rslt)

[print(*r, sep = "") for r in rslt_list]