N,M = map(int,input().split())
player = [i+1 for i in range(N)]
weak = []
strong = []
for i in range(M):
  y = False
  a,b = input().split()
  weak.append(b)

  for l in weak:
    if l == a:
      y = True

  if y == False:
    strong.append(a)
  
  for l in strong:
    if l == b:
      strong.remove(b)

if len(strong) == 1:
  print(strong[0])
else:
  print(-1)

# import sys
# input = sys.stdin.buffer.readline

# N, M = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(M)]
# player = [True] * N

# for i in range(M):
#   B = data[i][1]
#   player[B-1] = False

# if player.count(True) == 1:
#   print(player.index(True) + 1)
# else:
#   print(-1)